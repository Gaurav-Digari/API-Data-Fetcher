import requests
username=input("Enter Your Git-Hub Username : ")

url=f"https://api.github.com/users/{username}"
response=requests.get(url)
