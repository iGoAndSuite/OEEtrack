import automationhat
import time
from oeeRecords import *
from insertData import *
from uploadData import *

#adc1_anterior = False
adc2_anterior = False
adc3_anterior = False

def controlar_ADC(adc_anterior):
    
    # Habilitar el rango de voltaje automático del ADC
    automationhat.analog.one.auto_voltage_range = True

    # Establecer un umbral para encender y apagar el ADC
    umbral_encendido = 4.9
    #umbral_apagado = 4.0


    ADC1Act = automationhat.analog.one.read()
    #print("adc1_anterior= ")
    #print(adc1_anterior)
    if ADC1Act >=umbral_encendido and adc_anterior[0]==0:
            
        print("Pulso Input 1", ADC1Act)
        insertData()
        automationhat.analog.one.auto_voltage_range = True  # Encender el ADC
        adc_anterior[0] = True
        #print("flag set to true")
                #time.sleep(1)  # Esperar un segundo antes de volver a verificar
    else:
        if ADC1Act < umbral_encendido:
            automationhat.analog.one.auto_voltage_range = False  # Apagar el ADC
            adc_anterior[0] = False
            #print("flag set to False")
                #time.sleep(1)  # Esperar un segundo antes de volver a verificar
        else:
            adc_anterior[0] = True
            #print("flag set to true")
 
        
    ADC2Act = automationhat.analog.two.read()
        
    if ADC2Act >=umbral_encendido and adc_anterior[1]==0:
            
        print("Pulso Input 2", ADC2Act)
        insertData2()
        automationhat.analog.two.auto_voltage_range = True  # Encender el ADC
        adc_anterior[1] = True
        #time.sleep(1)  # Esperar un segundo antes de volver a verificar
    else:
        if ADC2Act < umbral_encendido:
            automationhat.analog.two.auto_voltage_range = False  # Apagar el ADC
            adc_anterior[1] = False
            #time.sleep(1)  # Esperar un segundo antes de volver a verificar
        else:
            adc_anterior[1] = True
   
      
    ADC3Act = automationhat.analog.three.read()
        
    if ADC3Act >=umbral_encendido and adc_anterior[2]==0:
            
        print("Pulso Input 3", ADC3Act)
        insertData3()
        automationhat.analog.three.auto_voltage_range = True  # Encender el ADC
        adc_anterior[2] = True
        #time.sleep(1)  # Esperar un segundo antes de volver a verificar
    else:
        if ADC3Act < umbral_encendido:
            automationhat.analog.three.auto_voltage_range = False  # Apagar el ADC
            adc_anterior[2] = False
            #time.sleep(1)  # Esperar un segundo antes de volver a verificar
        else:
            adc_anterior[2] = True

    return adc_anterior