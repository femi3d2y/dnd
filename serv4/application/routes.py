from flask import request
from application import app, db
from application.models import Effects
import requests

@app.route('/data', methods=['POST'])
def data():

        response = requests.post('http://flask-service:5001/service')
        hundred = response.json()['value']

        response1 = requests.post('http://flask-service2:5002/service2')
        ten = response1.json()['value']

        roll = int(ten) + int(hundred)

        if roll == 0:
            roll = 100
    
        effect = Effects.query.filter_by(id = roll).first()

        return {'result':'{}'.format(roll)}
