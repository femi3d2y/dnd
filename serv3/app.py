from flask import Flask
from application import dice

app = Flask(__name__)

@app.route('/ten', methods=['POST'])
def ten():

   num = die_10()

   return num

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
