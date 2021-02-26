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
output_df = pd.DataFrame()
# This is making an api call on each specific object and returning fields id & name
collected_data = []
for objects in data['objects']:
    object_name = str(objects['object'])
    url_id = url + object_name + "?" + "id&name__v"
    response = requests.request("GET", url_id, headers=headers, data=payload)
    json_file = response.json()
    print(json_file)
    object_name = json_file['responseDetails']['object']['label_plural']
    # print(object_name)
    json_parse = json_file['data']
    # print(json_parse)
    for x in json_parse:
        attribute = x['name__v']
        new_row = {object_name: attribute}
    #     collected_data.append(dict(zip(object_name, attribute)))
    #     # output_df = output_df.append(new_row, ignore_index= True)
    # output_df = pd.DataFrame(collected_data)


output_df.to_csv(r'C:/Users/CeciliaLuna/Documents/gsk_tool_output_3.csv', index = False)