valore_decimale_casuale = 0
quoziente_intero = 0
resto = 0
numero_binario = 0

def on_button_pressed_a():
    global valore_decimale_casuale, quoziente_intero, resto, numero_binario
    valore_decimale_casuale = randint(0, 9)
    quoziente_intero = Math.idiv(valore_decimale_casuale, 2)
    resto = valore_decimale_casuale % 2
    numero_binario = 0
input.on_button_pressed(Button.A, on_button_pressed_a)
