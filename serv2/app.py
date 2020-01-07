from flask import Flask
from dice import die_100

app = Flask(__name__)

@app.route('/service', methods=['POST'])
def service():

  hundred = die_100()


  return {'value':f'{hundred}'}
   


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
