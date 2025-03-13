'''
Programa que permita escribir, la tabla de multiplicar de un número dado (N). Ejm: la tabla del 9 mostrar:
9 * 1 = 9
9 * 2 = 18

9 * 10=90

ANALISIS:  
    ENTRADAS:  tabla
    PROCESOS:  resultado = tabla * ?  #bucle con contador de uno en uno
    SALIDAS :  resultado
'''
import libreria

#VARIABLES GLOBALES INICIALIZADAS
MINIMO = 1
MAXIMO = 20

tabla = 0
resultado = 0

#ENTRADAS
#tabla = libreria.validarEntero ( "TABLA DEL: ", MINIMO, MAXIMO)  #int(input("TABLA: "))
tabla = libreria.validarEntero ( "TABLA DEL: ", MINIMO) 

#BUCLE FOR PARA RECORRER DE 1 A 10
#[1]. MI VARIABLE DE CONTROL INICIA EN UN VALOR
for contador in range(1, 10, 1):
    #PROCESOS
    resultado = tabla * contador
    #SALIDAS
    print (f"{tabla} * {contador} = {resultado}")