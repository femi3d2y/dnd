from flask import render_template, request
from application import app


@app.route('/')
@app.route('/home', methods=['GET'])
def home():
    requests.get('URL of VM', json=num)

    requests.get('URL of VM', json=num)


    return render_template('home.html')

