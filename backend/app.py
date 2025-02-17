from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
#^ Enable CORS for all routes

@app.route('/')
def hello():
    return 'Hello world!'

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello from the backend!'})

if __name__ == '__main__':
    app.run(port=5000)