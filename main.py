quoziente_intero = 0
valore_decimale_casuale = 0
resto = 0
numero_binario = ""

def on_button_pressed_a():
    global quoziente_intero, valore_decimale_casuale, resto, numero_binario
    quoziente_intero = 1
    while quoziente_intero>0:
        valore_decimale_casuale = randint(0, 9)
        quoziente_intero = Math.idiv(valore_decimale_casuale, 2)
        resto = valore_decimale_casuale % 2
        numero_binario = "" + str(resto) + numero_binario
        valore_decimale_casuale = quoziente_intero
input.on_button_pressed(Button.A, on_button_pressed_a)
