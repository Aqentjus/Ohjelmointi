'''
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
'''

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='pythonuser',
         password='pythonpassword',
         autocommit=True
         )



def hae_tietokannasta(syote):
    sql = f"SELECT * FROM airport WHERE ident = '{syote}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos[0][3]


syote = str(input("Antaisitko lentokentän koodin?: "))
print(f'Haetun lentokentän koko nimi on: {hae_tietokannasta(syote)}')


