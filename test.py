from flask import Flask, request
import time

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def catch_all(path):
    print(f"Path: {path}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Params: {request.args}")
    print(f"Data: {request.data}")

    # Wait for 5 seconds
    time.sleep(5)

    return "yessir"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

