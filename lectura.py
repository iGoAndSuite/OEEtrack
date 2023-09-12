import automationhat
import time

bandera = 1

# Configura el ADC (Convertidor Analógico-Digital)
automationhat.analog.one.auto_voltage_range = True
voltaje_referencia = 5

while True:
# Realiza una única lectura del canal 1 del ADC
    ADC1 = automationhat.analog.one.read()
    if ADC1 >= voltaje_referencia  and bandera == 1:
        print("Leyendo")
        bandera = 0

    elif not ADC1 and bandera == 0:
        bandera = 1