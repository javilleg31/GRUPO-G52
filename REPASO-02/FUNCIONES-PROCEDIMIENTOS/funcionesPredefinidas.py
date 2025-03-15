#FUNCIONES O PROCEDIENTOS O METODOS PROPIOS DE PYTHON O DE UN TERCERO

print("soy un procedimiento")  # Procedimiento muestra en pantalla la etiqueta y puede llevar vaiables
#recibe = input("Ingrese: ")    # Funcion que retorna el valor ingresado x teclado

#funciones de cadena
cadena = "SOY UNA CADENA QUE ME APLICAN MÉTODOS"
print (type(cadena))

longitud = len(cadena)
mayusculas = cadena.upper()
minusculas = cadena.lower()
mayusculaInicial = cadena.capitalize()
quitarEspacios   = cadena.strip()

esNumerica   = cadena.isnumeric()
esAlfabetica = cadena.isalpha()
esDigito     = cadena.isdigit()
esDecimal    = cadena.isdecimal()

import  math
radicando = 4
raizCuadrada = math.sqrt( radicando )  # radicando ** 1 / 2
print(f"Raiz de {radicando} es {raizCuadrada}")

base = 2
exponente = 3
potenciaConAsterisco = base ** exponente
potenciaConPow = math.pow(base, exponente)
print(f"base de {base} potencia {exponente} = {potenciaConPow}")



