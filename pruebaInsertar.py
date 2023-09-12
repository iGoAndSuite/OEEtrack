from peewee import *
from oeeRecords import OeeRecord
import datetime
import time
from configurations import *

db = SqliteDatabase('OeeRecord.db')
date = datetime.datetime.now()
epoch_time = int(date.strftime('%s'))


pulso = OeeRecord(sensor = 1, eth_mac = DIRECCION_MAC, date = epoch_time,  date_time = date)
pulso.save()
print("Dato insertado")