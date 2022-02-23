def on_pin_pressed_p0():
    global numero_binario_inserito_da_utente
    basic.clear_screen()
    numero_binario_inserito_da_utente = "" + numero_binario_inserito_da_utente + "0"
    basic.show_string("" + (numero_binario_inserito_da_utente))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    basic.clear_screen()
    basic.show_string("" + (numero_binario_inserito_da_utente))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_pin_pressed_p2():
    basic.clear_screen()
    if numero_binario_inserito_da_utente == numero_binario:
        basic.show_icon(IconNames.HEART)
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . # # # .
                        # . . . #
                        # . . . #
        """)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_button_pressed_b():
    basic.clear_screen()
    basic.show_string("" + str(valore_decimale_da_convertire))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    global numero_binario_inserito_da_utente
    basic.clear_screen()
    numero_binario_inserito_da_utente = "" + numero_binario_inserito_da_utente + "1"
    basic.show_string("" + (numero_binario_inserito_da_utente))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

numero_binario_inserito_da_utente = ""
numero_binario = ""
resto = 0
valore_decimale_da_convertire = 0
quoziente_intero = 1
valore_decimale_casuale = randint(0, 9)
valore_decimale_da_convertire = valore_decimale_casuale
while quoziente_intero > 0:
    quoziente_intero = Math.idiv(valore_decimale_casuale, 2)
    resto = valore_decimale_casuale % 2
    numero_binario = "" + str(resto) + numero_binario
    valore_decimale_casuale = quoziente_intero
basic.show_string("" + str(valore_decimale_da_convertire))