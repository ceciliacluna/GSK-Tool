import requests
import json
import pandas as pd

# reading json file from directory
f = open('C:\\Users\\CeciliaLuna\\Documents\\1_GSK CONSUMER-ExtractObjectData.json')
data = json.load(f)
f.close()

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

url = 'https://sb-gskch-quality.veevavault.com/api/v19.1/vobjects/'

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


collected_data = {}
for objects in data['objects']:
    object_name = str(objects['object'])
    url_id = url + object_name + "?" + "id&sort=name__v asc"
    response = requests.request("GET", url_id, headers=headers, data=payload)
    json_file = response.json()
    print(json_file)
    object_name_resp = json_file['responseDetails']['object']['label_plural']
    print(object_name_resp, "Object name from response")
    json_parse = json_file['data']
    for x in json_parse:
        attribute = x['name__v']
        collected_data.setdefault(object_name_resp, []).append(attribute)


# add left template to table
complete_dict.update(collected_data)

new_output = pd.DataFrame.from_dict(complete_dict, orient='index')
new_output = new_output.transpose()
new_output.to_csv(r'C:/Users/CeciliaLuna/Documents/gsk_output_4.csv', index=False)

