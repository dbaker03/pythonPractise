import json
import requests
from pprint import pprint

pc_req = requests.get("https://api.postcodes.io/postcodes/SK8 2ER")

print(pc_req, type(pc_req))
# we get a response code Response [200] - this means everything is okay
# 404 is file not found
# anything in 200's is it has worked
# anything in 400's something has gone wrong

if pc_req.status_code == 200:  # can grab the status code
    pprint(dict(pc_req.headers), sort_dicts=False)  # headers is a dictionary
    pprint(pc_req.content)  # body is a byte stream - python converts these into characters for us but still bytes
    postcode = json.loads(pc_req.content)  # convert to dictionary using the json package
    print(postcode['result']['postcode'])
    postcode = pc_req.json()  # another way to convert to dictionary

    pprint(postcode, sort_dicts=False)
    print('admins district:', postcode['result']['admin_district'])
    print('eastings:', postcode['result']['eastings'])
    print('northings:', postcode['result']['northings'])
    print('nuts:', postcode['result']['codes']['nuts'])








print("\n" * 100)

headers = {'Content-Type': 'application/json'}
body = {'postcodes': ['SK82ER', 'SK82JA', "SW1A 1AA"]}

pc_req = requests.post(
    "https://api.postcodes.io/postcodes/",
    headers=headers,
    data=json.dumps(body)  # server expects a json dictionary
)

# print(pc_req.reason)  # if we get response in 400's we can check reason to help figure out issue
print(pc_req)
pcs = pc_req.json()
pprint(pcs, sort_dicts=False)

for r in pcs['result']:
    result = r['result']
    print(f"For code {result['postcode']}:")
    print(f"Admin ward: {result['admin_ward']}, Eastings: {result['eastings']}, Northings: {result['northings']}, Nuts code: {result['codes']['nuts']}\n")
