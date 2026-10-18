import api, requests, json

api.main()

url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
response = requests.get(url)
data = response.json()
json_str = json.dumps(data, indent=4)
#print(type(json_str))
json_data = json.loads(json_str)
print(type(json_data))
#print(json_data["data"])
print(json_data["data"]["location"].get('city'))