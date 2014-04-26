from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from bson.objectid import ObjectId
from bson import json_util
import json

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
	forms.save(form_data)

def get_all_forms():
	pass	
	

if __name__ == '__main__':
	pass
