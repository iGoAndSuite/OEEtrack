import socket
import fcntl
import struct

def get_upload_rate():
    return 10 #number of seconds between each upload


def get_activation_voltage():
    return 2 #Minimum voltage at input to be considered as an "ON" signal

def obtener_direccion_mac(interface):
    try:
        info = fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 0x8927, struct.pack('256s', interface[:15].encode('utf-8')))
        direccion_mac = ':'.join(['{:02x}'.format(b) for b in info[18:24]])
        return direccion_mac
    except Exception as e:
        print("Error al obtener la dirección MAC:", e)
        return None

# Cambia "eth0" por el nombre de la interfaz de red correspondiente en tu Raspberry Pi
nombre_interfaz = "eth0"
DIRECCION_MAC = obtener_direccion_mac(nombre_interfaz)

if DIRECCION_MAC:
    print("Dirección MAC de", nombre_interfaz, ":", DIRECCION_MAC)

API_ENDPOINT = "https://suite.goandsee.co/api/v3/oee"

