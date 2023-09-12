from configurations import *
from readData import *
from uploadData import *
import time
# Inicializar una variable para guardar estado anterior del ADC
adc_anterior = [False, False, False]


preset =60
cont=0
t_act=time.time()
t_ant=t_act
while True:



    t_act=time.time()
   
    adc_anterior=controlar_ADC(adc_anterior)
    if t_act-t_ant>6:
        request()    
        t_ant=t_act
  

    
