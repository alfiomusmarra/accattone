let quoziente_intero = 0
let valore_decimale_casuale = 0
let resto = 0
let numero_binario = ""
input.onButtonPressed(Button.A, function () {
    quoziente_intero = 1
    valore_decimale_casuale = randint(0, 9)
    while (quoziente_intero > 0) {
        quoziente_intero = Math.idiv(valore_decimale_casuale, 2)
        resto = valore_decimale_casuale % 2
        numero_binario = "" + resto + numero_binario
        valore_decimale_casuale = quoziente_intero
    }
    basic.showString(numero_binario)
})
