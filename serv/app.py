from flask import Flask, render_template, request
from forms import SubmitForm
from os import getenv
import requests

app = Flask(__name__)

app.config['SECRET_KEY']=getenv('KEY')


@app.route('/', methods=['GET', 'POST'])
def home():

    form = SubmitForm()

    if form.is_submitted():
        response = requests.post('http://flask-service:5001/service')
        if response.ok:
            return  response.json()['value']

      # response1 = requests.get('35.246.77.128:5002')
      # data1 = response1.json()

      # response2 = requests.get('35.246.77.128:5003')
      # data2 = response2.json()



    return render_template('home.html', form=form)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

