import requests
username=input("Enter Your Git-Hub Username : ")

url=f"https://api.github.com/users/{username}"

response=requests.get(url)


if response.status_code == 404:
    print("Username Not Found")
    exit()

response=response.json()

print("\n============================= \n GitHub User Info \n=============================\n")

print(f"username            : {response["login"]}")
print(f"Name                : {response["name"]}")
print(f"Public repos        : {response["public_repos"]}")
print(f"Followers           : {response["followers"]}")
print(f"Following           : {response["following"]}")
print(f"Profile URL         : {response["url"]}")
