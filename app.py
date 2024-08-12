from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
import requests
import json 

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route('/proxy', methods=['GET'])
@cross_origin(supports_credentials=True)
def getSummary():
    print(1)
    req = dict(request.headers)
    print(2)
    response = ''
    print(req.keys())
    if('Headers' in req.keys()):
        print("Head")
        response = requests.get(req['Url'],headers=json.loads(req['Headers']))
    
    else:
        response = requests.get(req['Url'])

    print(3)
    return response.text


@app.route('/')
def home():
    return "Hello!!"

if __name__ == "__main__":
    app.run()
