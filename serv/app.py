from flask import Flask, render_template, request
from forms import SubmitForm
from os import getenv
import requests

app = Flask(__name__)

app.config['SECRET_KEY']=getenv('KEY')


@app.route('/', methods=['GET', 'POST'])
def home():

    form = SubmitForm()

    hundred = ''
    ten =''

    if form.is_submitted():
        response = requests.post('http://flask-service:5001/service')
        hundred = response.json()['value']

        response1 = requests.post('http://flask-service2:5002/service2')
        ten = response1.json()['value']

      # response2 = requests.get('35.246.77.128:5003')
      # data2 = response2.json()



    return render_template('home.html', form=form, hundred=hundred, ten=ten)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

