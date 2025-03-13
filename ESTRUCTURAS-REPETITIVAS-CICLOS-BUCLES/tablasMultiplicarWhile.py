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
#VARIABLES GLOBALES INICIALIZADAS
tabla = 0
resultado = 0
final = 10

#ENTRADAS
tabla = int(input("TABLA: "))

#BUCLE FOR PARA RECORRER DE 1 A 10
#[1]. MI VARIABLE DE CONTROL INICIA EN UN VALOR
contador = 1    # 1 de 3
while (contador <= final):   #2 de 3 => mi varialbe control es comparada contra el valor final
    #PROCESOS
    resultado = tabla * contador
    #SALIDAS
    print (f"{tabla} * {contador} = {resultado}")

    contador = contador + 1  #3 de 3 =>  mi variable de control es incrementada o actualizada