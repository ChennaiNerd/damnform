from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from bson.objectid import ObjectId
from bson import json_util
import json
import uuid

client = MongoClient('mongodb://localhost:27017/')
db = client['damnform']
forms = db['forms']
entries = db['entries']

def is_valid_form_data(key, form_data):
	print "key = ", key
	print "form_data = ", form_data

def save_entry(key, form_data, labels):
	print "key = ", key
	print "form_data = ", form_data
	print "labels = ", labels
	entry = {}
	entries.save(entry)

def create_form(form_data):
	print "form_data = ", form_data
	dict_form_data = json.loads(form_data)
	dict_form_data['apikey'] = str(uuid.uuid4())
	_id = forms.save(dict_form_data)
	return json.dumps(forms.find_one({'_id': ObjectId(_id)}),  default=json_util.default)

def get_all_forms():
	return '[' + ', '.join([json.dumps(result, default=json_util.default) for result in forms.find()]) + ']'

if __name__ == '__main__':
	pass
