from peewee import SqliteDatabase, CharField, DateTimeField,IntegerField, FloatField, Model

db = SqliteDatabase('oeeRecord.db')

class OeeRecord(Model):
    sensor = IntegerField()
    eth_mac = CharField()
    epoch = FloatField()
    date_time = DateTimeField()

    class Meta:
        database = db

db.connect()
db.create_tables([OeeRecord])