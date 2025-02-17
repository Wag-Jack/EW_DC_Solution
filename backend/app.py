from flask import Flask, request, jsonify
from flask_cors import CORS

# Setup Flask and CORS for routing
app = Flask(__name__)
CORS(app)

#Predefined password, hide password until event?
PW = '3ng!neersWeek2o25!'

@app.route('/')
def hello():
    return "<p>Hi! I'm alive!</p>"

@app.route('/validate-password', methods=['POST'])
def validate_password():
    data = request.get_json()
    password = data.get('password')

    if password == PW:
        return jsonify({"success": True, "message": "Correct!"}), 200
    else:
        return jsonify({"success": False, "message": "Sorry, try again!"}), 200

if __name__ == '__main__':
    app.run() #Change port number in one of the branches?