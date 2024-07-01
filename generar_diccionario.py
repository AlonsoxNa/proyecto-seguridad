import keyboard
import hashlib

def hash_tecla(tecla_name):
    # Función para hashear la tecla usando SHA-256.
    return hashlib.sha256(tecla_name.encode()).hexdigest()

def detectar_tecla(tecla):
    with open('texto_hasheado.txt', 'a', encoding='utf-8') as archivo:
        archivo.write(f"{hash_tecla(tecla.name)}\n")
    # with open('diccionario_hashes.txt', 'a', encoding='utf-8') as archivo:
    #     archivo.write(f"{tecla.name}: {hash_tecla(tecla.name)}\n")

# Captura la tecla presionada y guarda su hash SHA-256
keyboard.on_press(detectar_tecla)

# Espera hasta que se presione 'esc' para detener la captura
keyboard.wait('esc')

"""import keyboard
import hashlib

def hash_tecla(tecla_name):
    # Función para hashear la tecla usando SHA-256.
    return hashlib.sha256(tecla_name.encode()).hexdigest()

def detectar_tecla(tecla):
    with open('teclas_cifradas.txt', 'a', encoding='utf-8') as archivo:
        archivo.write(f"{hash_tecla(tecla.name)}\n")

keyboard.on_press(detectar_tecla)

# Espera hasta que se presione 'esc' para detener el programa
keyboard.wait('esc')

print("Captura de teclas completada. Los hashes de las teclas presionadas se han guardado en 'teclas_cifradas.txt'.")
"""
