from flask import Flask
from dice import die_10

app = Flask(__name__)

@app.route('/service2', methods=['POST'])
def service2():

   ten = die_10()

   return {'value':f'{ten}'}

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
