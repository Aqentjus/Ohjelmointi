
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

#haetaan tietyn kentän kaikki tiedot tietokannasta, käyttäen lentokenttä tunnistetta esim. EFHK
'''
def hae_tietokannasta_tietyn_kentan_tiedot(syote):
    sql = """SELECT * FROM airport WHERE ident = %s"""
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (syote,))
    return kursori.fetchall()

syote = str(input("Antaisitko lentokentän koodin?: "))
data = hae_tietokannasta_tietyn_kentan_tiedot(syote)
print(data)
'''
#haetaan tietystä kentästä tietty tieto sarakkeen arvo (specific field from specific airport)
'''
def tietty_kentta_kentan_tiedoista(syote, kentta):
    sql = """SELECT * FROM airport WHERE ident = %s"""
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (syote,))
    data = kursori.fetchall()
    data = data[0][kentta]
    return data


print(tietty_kentta_kentan_tiedoista(syote="EFHK", kentta='latitude_deg'))
'''

'''
#laskee kahden lentoaseman välimatkan kilometreissä

def calculate_distance(airport1_code, airport2_code):
    sql = """SELECT * FROM airport WHERE ident = %s"""
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (airport1_code,))
    airport1_data = kursori.fetchall()

    sql = """SELECT * FROM airport WHERE ident = %s"""
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (airport2_code,))
    airport2_data = kursori.fetchall()

    lat1 = float(airport1_data[0]['latitude_deg'])
    lat2 = float(airport2_data[0]['latitude_deg'])
    lng1 = float(airport1_data[0]['longitude_deg'])
    lng2 = float(airport2_data[0]['longitude_deg'])
    first_airport = (lat1, lng1)
    second_airport = (lat2, lng2)
    return distance.distance(first_airport, second_airport)

print(calculate_distance(airport1_code="EFHK", airport2_code="EFHK"))

'''



