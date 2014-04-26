from flask import Flask, render_template, request, redirect, url_for
import database
import uuid
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
			new_entry, code = '', 404
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
		if not form:
			form, code = '', 404
		return form, code
	elif request.method == 'PUT':
		code = 200
		form = database.update_form(form_id, request.data)
		if not form:
			form, code = '', 404
		return form, code
	elif request.method == 'DELETE':
		code = 204
		form = database.delete_form(form_id)
		if not form:
			code = 404
		return '', code

#GET /api/forms/:id/entries?labels=
@app.route('/api/forms/<form_id>/entries', methods=["GET"])
def entries(form_id):
	'''
	Function to GET entries created using particular form
	'''
	if request.method == 'GET':
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
		if not entry:
			entry, code = '', 404
		return entry, code
	elif request.method == 'PUT':
		entry = database.update_entry(entry_id, request.data) 
		if not entry:
			entry, code = '', 404
		return entry, code
	elif request.method == 'DELETE':
		code = 204
		entry = database.delete_entry(entry_id)
		if not entry:
			code = 404
		return '', code
	
if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port = 8000)
