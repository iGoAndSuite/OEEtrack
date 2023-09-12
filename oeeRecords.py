from peewee import SqliteDatabase, CharField, DateTimeField,IntegerField, FloatField,DecimalField, TextField,TimestampField,Model

db = SqliteDatabase('oeeRecord.db')

class OeeRecord(Model):
    sensor = IntegerField()
    eth_mac = CharField()
    date = IntegerField(null = False)
    date_time = DateTimeField()

    class Meta:
        database = db

db.connect()
db.create_tables([OeeRecord])
print("Base de datos creada")