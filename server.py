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
	labels = request.args.get('labels')
	print labels
	print request.form
	print request.data
	if database.is_valid_form_data(key, request.form, request.data):
		return database.save_entry(key, request.form, request.data, labels), 201
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
		return database.get_form(form_id)
	elif request.method == 'PUT':
		return database.update_form(form_id, request.data)
	elif request.method == 'DELETE':
		database.delete_form(form_id)
		return '', 204

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port = 8000)
