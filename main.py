import requests
import json
import pandas as pd
import re

# reading json file from directory
input_path = "C:\\Users\\CeciliaLuna\\Documents\\Daelight Tool Box Helpful Documents\\Example Inputsheet.xlsx"

# authenticating
url = "https://sb-gskch-quality.veevavault.com/api/v20.3/auth"

payload = {'username': 'akunz@sb-gskch.com',
'password': 'Daffyduck123?'}
files = [

]
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("POST", url, headers=headers, params=payload, files=files)
authContent = response.json()
sessionID = authContent['sessionId']

obj_url = 'https://sb-gskch-quality.veevavault.com/api/v19.1/vobjects/'
picklist_url = 'https://sb-gskch-quality.veevavault.com/api/v19.1/objects/picklists/'
temp_url = "https://sb-gskch-quality.veevavault.com"

payload = {}
files = {}
headers = {
    'Accept': 'application/json',
    'Authorization': sessionID,
}

complete_dict = {
    "Agreement": ["Assessment", "Form", "Plan", "Policy_and_Procedure", "Protocol", "Quality_and_Audit", "Record", "Reference", "Report", "Specification", "Template", "Training"],
    "Field2": [],
    "Field3": [],
    "Field4": [],
    "Yes": ["No"],
    "Field6": [],
    "Restricted": ["Unrestricted"],
    "Field8": [],
    "Classification": [],
}

data = pd.read_excel(input_path)
collected_data = {}
for index, row in data.iterrows():
    object_name = str(row['Object'])
    url_id = obj_url + object_name + "?" + "id&sort=name__v asc"
    if object_name.startswith('picklist-'):
        picklist = object_name.removeprefix('picklist-')
        picklist_col_name = re.sub(r'[\W_]', ' ', picklist).removesuffix('c').title()
        picklist_url_id = picklist_url + picklist + "?" + "sort=label asc"
        picklist_response = requests.request("GET", picklist_url_id, headers=headers, data=payload)
        picklist_json_file = picklist_response.json()
        plist_json_parse = picklist_json_file['picklistValues']
        for x in plist_json_parse:
            label = x['label']
            collected_data.setdefault(picklist_col_name, []).append(label)
        continue
    while True:
        response = requests.request("GET", url_id, headers=headers, data=payload)
        json_file = response.json()
        object_name_resp = json_file['responseDetails']['object']['label_plural']
        json_parse = json_file['data']
        # print(json_file)
        for x in json_parse:
            attribute = x['name__v']
            collected_data.setdefault(object_name_resp, []).append(attribute)
        try:
            next_page = json_file['responseDetails']['next_page']
            url_id = temp_url + next_page
            if next_page is None or next_page == "":
                break
        except KeyError:
            break
# add left template to table
complete_dict.update(collected_data)

new_output = pd.DataFrame.from_dict(complete_dict, orient='index')
new_output = new_output.transpose()
new_output.to_csv(r'C:/Users/CeciliaLuna/Documents/gsk_output_test.csv', index=False)

