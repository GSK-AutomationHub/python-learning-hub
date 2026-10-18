import requests, json

url = "https://api.freeapi.app/api/v1/public/randomproducts"
header = {'content-type':'application/json'}
param = {'page': 1, 'limit' : 1 }
file_path = ".\\python_file_io\\get_product.json"


def get_product_request(url, header, param):
    response = requests.get(url=url, headers=header, params=param)
    print(response.status_code)
    if response.json()["data"]["data"][0].get('title') == 'iPhone 9':
        print("---> assertion for product title passed successfully")
    else:
        print("---> assertion for product title failed")
    return response.json()


def dump_response_to_json_file(api_response, path_to_file):
    with open(path_to_file, 'a') as file:
        json.dump(api_response, file, indent=4)


response_data = get_product_request(url, header, param)
dump_response_to_json_file(response_data, file_path)


def load_json_file(path_to_file):
    with open(path_to_file, 'r') as file:
        return json.load(file)


print(json.dumps(load_json_file(file_path), indent=4))