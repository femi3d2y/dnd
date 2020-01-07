from flask import Flask

app = Flask(__name__)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)

@app.route('/', methods=['GET', 'POST'])
def home():
	requests.get('URL of VM', json=hundred)

    	requests.get('URL of VM', json=ten)

