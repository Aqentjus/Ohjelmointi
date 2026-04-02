from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentokone_peli',
         user='lentokone_peli_user',
         password='SuperSalain3nSalasna1234#',
         autocommit=True
         )

def get_airport_by_indent(ident):
    sql = "SELECT * FROM airport WHERE ident = %s"
    cursor = yhteys.cursor(dictionary=True)
    cursor.execute(sql, (ident,))
    return cursor.fetchone()


# http://127.0.0.1:3000/alkuluku/
@app.route('/kenttä/<icao>')
def alkuluku(icao):
    icao = str(icao)
    data = get_airport_by_indent(icao)
    response = {
        "ICAO": data['ident'],
        "Name": data['name'],
        "Municiability": data['municipality'],
    }
    return jsonify(response)

app.run(use_reloader=True, host='127.0.0.1', port=3000)
