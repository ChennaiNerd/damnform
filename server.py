from flask import Flask, render_template, request, redirect, url_for
from werkzeug import MultiDict
import database
import uuid
import json
import mailgun
import hashlib
app = Flask(__name__, static_folder='client', static_url_path='')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/app', methods=["POST", "GET"])
def default_app():
	if request.method == "GET":
		return app.send_static_file('app.html')
	elif request.method == "POST":
		return redirect(url_for('default_app'))

@app.route('/thankyou.html')
def show_thank_you():
	return app.send_static_file('thankyou.html')

#POST /api/:key?labels=:labels
@app.route('/api/<key>', methods=["POST"])
def create_entry(key):
	''' 
	This url will be used by the admin user for creating entry
	'''
	code = 201
	labels = request.args.get('labels')
	if database.is_valid_form_data(key, request.form, request.data):
		new_entry = database.save_entry(key, request.form, request.data, labels)
		if not new_entry:
			return '', 404
		if not request.data:
			email_field = database.get_email_field(key)
			welcome_mail_info = database.get_welcome_mail_info(key)
			send_welcome_mail(new_entry[email_field], welcome_mail_info)

			redirect_url = database.get_thankyou_url(key)
			if redirect_url:
				return redirect(redirect_url)
			else:
				return redirect(url_for('show_thank_you'))
		return new_entry, code
	else:
		return "Invalid form data", 400

#GET, POST /api/forms
@app.route('/api/forms', methods=["POST", "GET"])
def forms():
	'''
	Function to create forms
	'''
	if request.method == 'POST':
		return database.create_form(request.data), 201
	elif request.method == 'GET':
		return database.get_all_forms()

#GET, PUT, DELETE /api/forms/:id
@app.route('/api/forms/<form_id>', methods=["GET", "PUT", "DELETE"])
def form(form_id):
	'''
	Function to do GET, PUT, DELETE on a particular form
	'''
	if request.method == 'GET':
		code = 200
		form = database.get_form(form_id)
	elif request.method == 'PUT':
		code = 200
		form = database.update_form(form_id, request.data)
	elif request.method == 'DELETE':
		code = 204
		form = database.delete_form(form_id)

	if not form:
		form, code = '', 404

	return form, code

#GET /api/forms/:id/entries?labels=
@app.route('/api/forms/<form_id>/entries', methods=["GET"])
def entries(form_id):
	'''
	Function to GET entries created using particular form
	'''
	labels = request.args.get('labels')
	return database.get_entries(form_id, labels)	

#GET, PUT, DELETE /api/forms/:id/entries/:id
@app.route('/api/forms/<form_id>/entries/<entry_id>', methods=["GET", "PUT", "DELETE"])
def entry(form_id, entry_id):
	'''
	Function to GET, PUT, DELETE a single entry
	'''
	if request.method == 'GET':
		code = 200
		entry = database.get_entry(entry_id)
	elif request.method == 'PUT':
		code = 200
		entry = database.update_entry(entry_id, request.data) 
	elif request.method == 'DELETE':
		code = 204
		entry = database.delete_entry(entry_id)
	
	if not entry:
		entry, code = '', 404

	return entry, code

#GET /avatar/:email
@app.route('/avatar/<email_id>', methods=["GET"])
def getGravatar(email_id):
	'''
	Function to calculate the md5 hash of email_id & return gravatar image URL
	'''
	m = hashlib.md5()
	m.update(email_id)
	myhash = m.hexdigest()
	url = 'https://gravatar.com/avatar/' + myhash
	return redirect(url)

#POST /api/forms/:id/sendmail
app.route('/api/forms/<form_id>/sendmail', methods=["POST"])
def sendmail(form_id):
	'''
	Function to send mail to entries under form based on label criteria
	'''
	mail_info = json.loads(request.data)
	mail = compose_mail(mail_info['to'], mail_info['subject'], mail_info['message'])
	mailgun.send_simple_message(mail)

def compose_mail(to, subject, message):
	return {
				"from": "Mailgun Sandbox <postmaster@sandbox381bc65cf9a0430cb057afb272d83c3a.mailgun.org>",
				"to": str(','.join(to)),
				"subject": subject,
				"text": message
				#"html": "<html>Testing HTML <b>Bold</b><i>Italics</i><u>Underline</u></html>"
			}

def send_welcome_mail(welcome_mail_info):
	#compose_mail(
	pass
	
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port = 8000)
