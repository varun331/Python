from flask import Flask, render_template, request, jsonify
#from processing import display_recepie
from processing import receipe
from flask_mail import Mail,Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'stylish992@gmail.com'
app.config['MAIL_PASSWORD'] = 'xxxxxx'

mail=Mail(app)

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
	#email = s.email_msg()
	#output = 'varun'
	#if name and email:
		#newName = name[::-1]
	#if output:
			
		#return jsonify({'name' : newName})
	return jsonify({'name':output})
	#return (output)	
	#return jsonify({'error' : 'Missing data!'})
@app.route('/email', methods=['POST'])
def email():

	output = request.form['output']   
	result = 'Email sent to varun331@gmail & deepti.sahu@gmail.com'
	
	#s = receipe()
	
	msg=Message('test email',sender='stylish992@gmail.com',recipients=['varun331@gmail.com','deepti.sahu@gmail.com'],body=output)
	mail.send(msg)
	return jsonify({'name':result})

if __name__ == '__main__':
	app.run(debug=True)