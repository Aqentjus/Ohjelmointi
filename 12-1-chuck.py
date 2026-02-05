'''
Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle. 
Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/. Käyttäjälle on näytettävä pelkkä vitsin teksti.
'''

import requests

api = "https://api.chucknorris.io/jokes/random"

request = requests.get(api).json()
print(request['value'])
