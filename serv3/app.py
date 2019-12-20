from flask import Flask
from dnd_magic import dice

app = Flask(__name__)

@app.route('/ten')
def ten():

   num = die_10()

   return num

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
