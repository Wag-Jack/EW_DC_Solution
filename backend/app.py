from flask import Flask, request, jsonify
from flask_cors import CORS

# Setup Flask and CORS for routing
app = Flask(__name__)
CORS(app)

#Password will be hidden in README.md lemme cook
PW = 'apple'

@app.route('/')
def hello():
    return "<p>The answer hides in bold.</p>" #Come up with something more creative later

@app.route('/', methods=['POST'])
def validate_password():
    data = request.get_json()
    password = data.get('password')
    print(f'Recieved password: {password}')

    if password == PW:
        return jsonify({"success": True, "message": "Correct!"}), 200
    else:
        return jsonify({"success": False, "message": "Sorry, try again!"}), 401

if __name__ == '__main__':
    app.run(port=5000) #Change port number in one of the branches?