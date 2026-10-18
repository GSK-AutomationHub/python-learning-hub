import requests, json

url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'

def fetch_username_from_freeapi(url):
    response = requests.get(url)
    data = response.json()
    if data["success"] is True and "data" in data:
        username = data["data"]["login"]["username"]
        country = data["data"]["location"]["country"]
        return username, country
    # else:
    #     raise Exception("something went wrong")



def main():
    try:
        username, country = fetch_username_from_freeapi(url)
        print(f"username:{username} \ncountry:{country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
else:
    print("something went wrong")
        

