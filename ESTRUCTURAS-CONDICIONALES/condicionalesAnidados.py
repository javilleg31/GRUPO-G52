'''
LEER 4 NUMEROS E INDICAR AL FINAL CUAL ES EL NUMERO MAYOR
ANALISIS
    ENTRADAS: numero1, numero2, numero3, numero4
    PROCESOS: mayor = numero1   ??? numero1 sea mayor a todos
              mayor = numero2   ??? numero2 sea mayor a todos
              mayor = numero3   ??? numero3 sea mayor a todos
              mayor = numero4   ??? numero4 sea mayor a todos
    SALIDAS : mayor
'''
import libreria

def leerNumero( etiqueta ):
    return float(input( etiqueta ))

def encontrarMayor ( numero1, numero2, numero3, numero4 ):
    if (numero1 > numero2 and numero1 > numero3 and numero1 > numero4):
        mayor = numero1
    elif (numero2 > numero3 and numero2 > numero4):
        mayor = numero2
    elif (numero3 > numero4):
        mayor = numero3
    else:
        mayor = 4

    return mayor

def generarSalida (numero1, numero2, numero3, numero4, mayor):
    print("NUMERO1 NUMERO2 NUMERO3 NUMERO4 MAYOR")
    print(f"{numero1} \t {numero2}  \t {numero3}  \t {numero4}  \t {mayor}")

#AQUI INICIA EL PROGRAMA
libreria.limpiarPantalla()

#VARIABLES GLOBALES INICIALIZADAS
numero1=0
numero2=0
numero3=0
numero4 = 0
mayor = 0

#ENTRADAS
numero1 = leerNumero ( "NUMERO 1: " )
numero2 = leerNumero ( "NUMERO 2: " )
numero3 = leerNumero ( "NUMERO 3: " )
numero4 = leerNumero ( "NUMERO 4: " )

#PROCESOS
mayor = encontrarMayor ( numero1, numero2, numero3, numero4 )

#GENERA SALIDAS
generarSalida (numero1, numero2, numero3, numero4, mayor)

#limpiar pantalla al finalizar
#libreria.mensajeEsperaSegundos( "Saliendo del Programa - Gracias por Utilizarnos", 2 )  #espera un segunto para ver el resultado
libreria.mensajeEsperaEnter ( "Gracias por Utilizarnos ENTER Salir de programa")
libreria.limpiarPantalla()
