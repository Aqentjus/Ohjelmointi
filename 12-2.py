'''
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. 
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina. 
Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key). 
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
'''

import requests

paikkakunta = str(input("Antaisitko paikkakunnan?> "))

request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid=35fb99549cdf67fc4921324c0664a776&units=metric").json()

print(request['weather']['description'])
print(request['main']['temp'])

#830232590afe8b6476d6c3c220c0c944
