import geopy


import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='pythonuser',
         password='pythonpassword',
         autocommit=True
         )


def hae_tietokannasta(syote):
    sql = """
        SELECT name, latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s
    """
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (syote,))
    return kursori.fetchall()

syote = str(input("Antaisitko lentokentän koodin?: "))
data = hae_tietokannasta(syote)
eka_kentta_nimi = data[0]['name']
eka_kentta_latitude = data[0]['latitude_deg']
eka_kentta_longitude = data[0]['longitude_deg']


syote = str(input("Antaisitko tokan lentokentän koodin?: "))
data = hae_tietokannasta(syote)
toka_kentta_nimi = data[0]['name']
toka_kentta_latitude = data[0]['latitude_deg']
toka_kentta_longitude = data[0]['longitude_deg']


eka_kentta_sijainti = (eka_kentta_latitude, eka_kentta_longitude)
toka_kentta_sijainti = (toka_kentta_latitude, toka_kentta_longitude)
matka = distance.distance(eka_kentta_sijainti, toka_kentta_sijainti)
print(f'lentokentän {eka_kentta_nimi} ja {toka_kentta_nimi} välinen matka on{matka}')




