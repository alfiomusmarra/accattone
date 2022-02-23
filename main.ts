input.onPinPressed(TouchPin.P0, function () {
    basic.clearScreen()
    numero_binario_inserito_da_utente = "" + numero_binario_inserito_da_utente + "0"
    basic.showString("" + (numero_binario_inserito_da_utente))
})
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.showString("" + (numero_binario_inserito_da_utente))
})
input.onPinPressed(TouchPin.P2, function () {
    basic.clearScreen()
    if (numero_binario_inserito_da_utente == numero_binario) {
        basic.showIcon(IconNames.Heart)
    } else {
        basic.showLeds(`
            . . . . .
            . . . . .
            . # # # .
            # . . . #
            # . . . #
            `)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    basic.showString("" + (valore_decimale_da_convertire))
})
input.onPinPressed(TouchPin.P1, function () {
    basic.clearScreen()
    numero_binario_inserito_da_utente = "" + numero_binario_inserito_da_utente + "1"
    basic.showString("" + (numero_binario_inserito_da_utente))
})
let numero_binario_inserito_da_utente = ""
let numero_binario = ""
let resto = 0
let valore_decimale_da_convertire = 0
let quoziente_intero = 1
let valore_decimale_casuale = randint(0, 9)
valore_decimale_da_convertire = valore_decimale_casuale
while (quoziente_intero > 0) {
    quoziente_intero = Math.idiv(valore_decimale_casuale, 2)
    resto = valore_decimale_casuale % 2
    numero_binario = "" + resto + numero_binario
    valore_decimale_casuale = quoziente_intero
}
basic.showString("" + (valore_decimale_da_convertire))
