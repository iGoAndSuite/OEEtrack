import requests
from oeeRecords import OeeRecord
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
        'date': record.date,
        'sensor': record.sensor,
        'eth_mac': record.eth_mac,
        'date_time': record.date_time.strftime('%Y-%m-%d %H:%M:%S'),
        #'epoch_date': str(record.date.timestamp())
    }
    return temp_object
#int(record.date.timestamp())

records = OeeRecord.select()




def upload_and_delete():
    records = OeeRecord.select()

    # Procesa cada registro y agrega los datos procesados a dataToSend
    dataToSend = []

    for record in records:
        dataToSend.append(to_remote_object(record))

    # Realiza la solicitud POST a la API
    try:
        response = requests.post(API_ENDPOINT, json=dataToSend)
        response.raise_for_status()
        if response.status_code == 200:
            print(f"Datos subidos exitosamente. Código de estado: {response.status_code}")
            deleteRecords()  # Elimina los registros de la base de datos
        else:
            print(f"Error al subir datos. Código de estado: {response.status_code}")
    except requests.exceptions.HTTPError as errh:
        print ("Error HTTP:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Error de conexión:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Error de timeout:",errt)
    except requests.exceptions.RequestException as err:
        print ("Error en la solicitud:",err)






