from peewee import *
from oeeRecords import *
import json
from bson import json_util
import arrow
from configurations import API_ENDPOINT
import requests



records = OeeRecord.select().dicts()
for row in records:
    #print(row)
    json_object = json.dumps(row,indent = 4, sort_keys=True, default=str)

    #print(json_object)
    
    #post_request = requests.post(url = API_ENDPOINT, json = json_object)

#print(post_request)
    

    
#for json_object in row:
    
#json_object = json.dumps(row, indent = 4, sort_keys=True, default=str) 
#print(json_object)