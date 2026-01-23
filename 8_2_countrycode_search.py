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
    sql = f"SELECT type FROM airport WHERE iso_country = '{syote}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos


closed = 0
small_airport = 0
medium_airport = 0
large_airport = 0
heliport = 0


syote = str(input("Antaisitko lentokentän koodin?: "))
tulos = hae_tietokannasta(syote)


for row in tulos:
    airport_type = row[0]   # <-- get string from tuple

    if airport_type == "closed":
        closed += 1
    elif airport_type == "small_airport":
        small_airport += 1
    elif airport_type == "medium_airport":
        medium_airport += 1
    elif airport_type == "large_airport":
        large_airport += 1
    elif airport_type == "heliport":
        heliport += 1



print(f'Suljettuja lentokenttiä: {closed}')
print(f' Pieniä lentokenttiä: {small_airport}')
print(f'Keskikokoisia lentokenttiä: {medium_airport}')
print(f'Isoja lentokenttiä: {large_airport}')
print(f'Helikopteri kenttiä: {heliport}')