from oeeRecords import *
from peewee import *
import datetime
import time
from configurations import *

def insertData(sensor):
    db = SqliteDatabase('OeeRecord.db')
    date = datetime.datetime.now()
    #epoch_time = int(date.strftime('%s'))
    epoch_time = int(date.timestamp()*1000)
    pulso = OeeRecord(sensor = sensor, eth_mac = DIRECCION_MAC, date = epoch_time,  date_time = date)
    pulso.save()
    #print("Dato insertado")