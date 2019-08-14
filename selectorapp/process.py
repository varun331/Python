from flask import Flask, render_template, request, jsonify
#from processing import display_recepie
from processing import receipe
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
#@app.route('/', methods=['POST'])
def process():

	#email = request.form['email']
	#name = request.form['name']
	s = receipe()
	output=s.display_recepie()
	#output = 'varun'
	#if name and email:
		#newName = name[::-1]
	#if output:
			
		#return jsonify({'name' : newName})
	return jsonify({'name':output})
	#return (output)	
	#return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
	app.run(debug=True)