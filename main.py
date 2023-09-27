from configurations import *
from readData import *
from uploadData import *
import time
from threading import Thread

def main():
    adc_anterior = [False, False, False] # Inicializar una variable para guardar estado anterior del ADC
    preset = get_upload_rate() #obtiene el valor necesario a esperar para subir informacion
    t_act=time.time()
    t_ant=t_act
    while True:
        t_act=time.time()
        adc_anterior = controlar_ADC(adc_anterior) #captura datos de las entradas analogas
        if t_act-t_ant>preset: #verifica que sea momento de subir datos
            t = Thread(target = upload_and_delete())
            t.start()
            t_ant=t_act
  
if __name__ == "__main__":
    main()
    