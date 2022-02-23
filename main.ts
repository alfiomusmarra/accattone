input.onButtonPressed(Button.A, function () {
	
})
input.onButtonPressed(Button.B, function () {
    if (switch_mostra_nascondi_decimale == 0) {
        basic.clearScreen()
        switch_mostra_nascondi_decimale = 1
    } else {
        basic.showString("" + (valore_decimale_da_convertire))
        switch_mostra_nascondi_decimale = 0
    }
})
let numero_binario = ""
let resto = 0
let valore_decimale_da_convertire = 0
let switch_mostra_nascondi_decimale = 0
switch_mostra_nascondi_decimale = 0
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
