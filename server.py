from flask import Flask, render_template, request
import database
import uuid
app = Flask(__name__, static_folder='client', static_url_path='')

@app.route('/')
@app.route('/app.html')
def index():
	return app.send_static_file('index.html')



#POST /api/:key?labels=:labels
@app.route('/api/<key>', methods=["POST"])
def create_entry(key):
	''' 
	This url will be used by the admin user for creating entry
	'''
	labels = request.args.get('labels')
	print labels
	print request.form
	if database.is_valid_form_data(key, request.form):
		return database.save_entry(key, request.form, labels)
	else:
		return "Invalid form data", 400

#GET, POST /api/forms
@app.route('/api/forms', methods=["POST", "GET"])
def forms():
	'''
	Function to create forms
	'''
	if request.method == 'POST':
		return database.create_form(request.form)
	elif request.method == 'GET':
		return database.get_all_forms()

if __name__ == '__main__':
	app.run(debug = True, host = '0.0.0.0', port = 8000)
