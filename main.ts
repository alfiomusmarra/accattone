let valore_decimale_casuale = 0
let quoziente_intero = 0
let resto = 0
let numero_binario = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    valore_decimale_casuale = randint(0, 9)
    quoziente_intero = Math.idiv(valore_decimale_casuale, 2)
    resto = valore_decimale_casuale % 2
    numero_binario = 0
})
