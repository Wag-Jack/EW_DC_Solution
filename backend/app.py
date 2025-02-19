from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

import base64 as b #hide

# Setup Flask and CORS for routing
app = Flask(__name__)
CORS(app)

#Password will be hidden in README.md lemme cook
with open('pw.txt', 'r') as pw:
    PW = b.b16decode(b.b32decode(b.b32hexdecode(b.b64decode(b.b85decode(pw.read().strip()))))).decode('utf-8')
    print(PW)

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
    print(f'Recieved password: {password}')

    if password == PW:
        print('Correct password!')
        return jsonify({"success": True, "message": "Correct!"}), 200
    else:
        print('Incorrect password')
        return jsonify({"success": False, "message": "Incorrect..."}), 401

if __name__ == '__main__':
    app.run(port=5000) #Change port number in one of the branches?