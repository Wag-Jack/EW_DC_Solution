import base64 as b
import builtins
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from pw import pw

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    #open file here and return the decoded base64 string to print
    with open('hint.txt', 'r') as file:
        decoded = b.b64decode(file.read().strip()).decode('utf-8')

        html_content = '''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>Riddle Time!</title>
          </head>
          <body>
            <pre>{{ content }}</pre>
          </body>
        </html>
        '''
        return render_template_string(html_content, content=decoded)
    
@app.route('/validate_password', methods=['POST'])
def validate_password():
    data = request.get_json()
    password = data.get('password')

    if password == os.getenv('PW'):
        return jsonify({"success": True, "message": "Correct!"}), 200
    else:
        return jsonify({"success": False, "message": "Incorrect..."}), 401

if __name__ == '__main__':
    app.run(port=5000) #Change port number in one of the branches?