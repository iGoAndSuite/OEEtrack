from peewee import *
from oeeRecords import OeeRecord
import datetime
import time
db = SqliteDatabase('OeeRecord.db')
date = datetime.datetime.now
epoch_time = time.time()



pulso = OeeRecord(sensor = 1, eth_mac = 1, epoch = epoch_time, date_time = date)
pulso.save()
print("Dato insertado")