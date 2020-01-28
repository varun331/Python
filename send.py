from flask import Flask
from flask_mail import Mail,Message

app=Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'stylish992@gmail.com'
app.config['MAIL_PASSWORD'] = 'eicc1q2q'

mail=Mail(app)

@app.route('/')
def index():
	result = 'Test email'
	msg=Message(result,sender='stylish992@gmail.com',recipients=['varun331@gmail.com'],body='You recipe selections')
	mail.send(msg)
	return 'Email sent'

if __name__ == '__main__':
	app.run(debug=True)


