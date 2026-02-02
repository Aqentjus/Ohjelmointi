from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# http://127.0.0.1:3000/alkuluku/2038
@app.route('/alkuluku/<int:number>')
def alkuluku(number):
    prime = is_prime(number)
    response = {
        "Number": number,
        "isPrime": prime
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
