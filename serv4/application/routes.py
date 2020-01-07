from flask import request
from application import app, db
from application.models import Effects


@app.route('/data', methods=['POST'])
def service4():
    response = requests.get('35.246.77.128:5001')
    data = response.json()

    response1 = requests.get('35.246.77.128:5002')
    data1 = response1.json()

    value = data + data1

    if value == 0:
        value = 100
    
    effect = Effects.query.filter_by(id = value)

    return effect
