import requests
from oeeRecords import OeeRecord  # Asegúrate de importar la clase OeeRecord correctamente
from configurations import API_ENDPOINT
import json
from datetime import datetime
import time


def deleteRecords():
    OeeRecord.delete().execute()
    print("Datos eliminados")


def to_remote_object(record): 
    temp_object = {
        'id': record.id,
        'sensor': record.sensor,
        'eth_mac': record.eth_mac,
        'date': record.date,
        'date_time': record.date_time.strftime('%Y-%m-%d %H:%M:%S'),
        #'epoch_date': str(record.date.timestamp())
    }
    return temp_object
#int(record.date.timestamp())

records = OeeRecord.select()
# Inicializa una lista vacía para almacenar los datos procesados
dataToSend = []
# Procesa cada registro y agrega los datos procesados a dataToSend
for record in records:
    dataToSend.append(to_remote_object(record))
    # Convierte dataToSend a un objeto JSON
    json_object = json.dumps(dataToSend, indent=4, sort_keys=True, default=str)
    #print(json_object)


def request():
    tiempo_maximo = 5  # Cambia este valor al tiempo deseado
    contador = 0
    if contador >= tiempo_maximo:
        print("Subiendo datos a la nube")
        print(contador)
        contador += 1
        time.sleep(1)
        req = requests.post(url=API_ENDPOINT, json=dataToSend)
        print(req)
    if req.status_code == 200:
        deleteRecords()
    else:
        print("No se eliminaron los registros")






