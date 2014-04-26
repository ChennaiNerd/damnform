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

def is_valid_form_data(key, value_in_form, value_in_data):
	#FIXME: Validate form_data with schema
	return True

def save_entry(apikey, value_in_form, value_in_data, labels):
	print "apikey = ", apikey
	print "value_in_form = ", value_in_form 
	print "value_in_data = ", value_in_data
	print "labels = ", labels
	if value_in_form:
		dict_form_data = value_in_form
	elif value_in_data:
		dict_form_data = json.loads(value_in_data)
	dict_form_data["form_id"] = get_form_id(apikey)
	dict_form_data["labels"] = labels
	_id = entries.save(dict_form_data)
	return json.dumps(entries.find_one({'_id': ObjectId(_id)}), default=json_util.default)

def create_form(form_data):
	print "form_data = ", form_data
	dict_form_data = json.loads(form_data)
	dict_form_data['apikey'] = str(uuid.uuid4())
	_id = forms.save(dict_form_data)
	return json.dumps(forms.find_one({'_id': ObjectId(_id)}), default=json_util.default)

def get_all_forms():
	return '[' + ', '.join([json.dumps(result, default=json_util.default) for result in forms.find()]) + ']'

def get_form_id(apikey):
	return str(forms.find_one({'apikey':apikey})['_id'])
	 
def get_form(form_id):
	return json.dumps(forms.find_one({'_id': ObjectId(form_id)}), default=json_util.default)

def update_form(form_id, form_data):
	return forms.find_and_modify(query={'_id': ObjectId(form_id)}, update=json.loads(form_data), new=True)
	
def delete_form(form_id):
	return forms.find_and_modify(query={'_id': ObjectId(form_id)}, remove=True)

def get_entries(form_id, labels):
	resultlist = []
	resultset = entries.find({'form_id': form_id, 'labels' : {'$in': labels.split(',')}})
	for result in resultset:
		resultlist.append(json.dumps(result, default=json_util.default))
	return '[' + ', '.join(resultlist) + ']'
 
if __name__ == '__main__':
	pass
