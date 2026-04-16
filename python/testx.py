import requests

api = "https://api.chucknorris.io/jokes/random"

print(requests.get(api).json())
