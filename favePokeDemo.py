import requests

choice = input("what's your favorite pokemon? ") 

url =  "https://pokeapi.co/api/v2/pokemon/"

fullUrl = url + choice

resp = requests.get(fullUrl)

print(resp.status_code)
if resp.status_code ==200:
    print("success")
print(resp.text)
print(fullUrl)



pokedata = resp.json()
