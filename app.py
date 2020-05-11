from flask import Flask, jsonify, render_template, request, make_response

app = Flask(__name__)

@app.route('/data')
def senddatajavascript():
    return render_template('index.html')

@app.route('/data/proses', methods=['POST'])
def prosesdata():
    req = request.get_json()
    phonenumber = req['phonenumber']
    print(phonenumber)
    res = make_response(jsonify({'message': 'JSON data received'}), 200)
    return res

app.run()