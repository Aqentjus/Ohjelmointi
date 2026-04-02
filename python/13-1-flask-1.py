from flask import Flask, jsonify

app = Flask(__name__)

def on_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# http://127.0.0.1:3000/alkuluku/
@app.route('/alkuluku/<int:number>')
def alkuluku(number):
    prime = on_alkuluku(number)
    response = {
        "Number": number,
        "isPrime": prime
    }
    return jsonify(response)

app.run(use_reloader=True, host='127.0.0.1', port=3000)
