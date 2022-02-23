def on_pin_pressed_p0():
    basic.clear_screen()
    numero_binario_inserito_da_utente = "" + numero_binario + "0"
    basic.show_string("" + str((numero_binario_inserito_da_utente)))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global switch_mostra_nascondi_decimale, switch_mostra_nascondi_binario
    if switch_mostra_nascondi_binario == 0:
        basic.clear_screen()
        switch_mostra_nascondi_decimale = 1
    else:
        switch_mostra_nascondi_binario = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global switch_mostra_nascondi_decimale
    if switch_mostra_nascondi_decimale == 0:
        basic.clear_screen()
        switch_mostra_nascondi_decimale = 1
    else:
        basic.show_string("" + str((valore_decimale_da_convertire)))
        switch_mostra_nascondi_decimale = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_pin_pressed_p1():
    basic.clear_screen()
    numero_binario_inserito_da_utente = "" + numero_binario + "1"
    basic.show_string("" + str((numero_binario_inserito_da_utente)))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

switch_mostra_nascondi_binario = 0
numero_binario = ""
resto = 0
valore_decimale_da_convertire = 0
switch_mostra_nascondi_decimale = 0
switch_mostra_nascondi_decimale = 0
quoziente_intero = 1
valore_decimale_casuale = randint(0, 9)
valore_decimale_da_convertire = valore_decimale_casuale
while quoziente_intero > 0:
    quoziente_intero = Math.idiv(valore_decimale_casuale, 2)
    resto = valore_decimale_casuale % 2
    numero_binario = "" + str(resto) + numero_binario
    valore_decimale_casuale = quoziente_intero
basic.show_string("" + str((valore_decimale_da_convertire)))