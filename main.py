def on_button_pressed_a():
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if switch_mostra_nascondi_decimale==0:
        pass
    basic.show_string("" + str((valore_decimale_da_convertire)))
input.on_button_pressed(Button.B, on_button_pressed_b)

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