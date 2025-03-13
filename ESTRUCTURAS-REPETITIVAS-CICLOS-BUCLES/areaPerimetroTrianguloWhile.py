'''
Planteamiento de Problema: Desarrollar un programa en Lenguaje Python, que permita hallar el área y perímetro de cualquier triángulo, utilizando funciones, para las entradas, procesos y salidas:
Restricciones para calcular el área NO se requiere de la altura
perimetro = lado1 + lado2 + lado3
'''
import math
import libreria
from colorama import Fore, Back, Style, init
#Inicializar colorama
init()

#FUNCIONES
def calcularPerimetro( lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def calcularArea( lado1, lado2, lado3 ):
    semiperimetro = (lado1 + lado2 + lado3) / 2
    area = math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))
    return area

def mostrarPerimetro(lado1, lado2, lado3, perimetro):
    print("*" * 50)
    print(" LADO1    LADO2    LADO3  PERIMETRO")
    print("*" * 50)
    print(f"{lado1} \t {lado2} \t {lado3} \t {perimetro}") 

def mostrarArea(lado1, lado2, lado3, area):
    print("*" * 50)
    print(" LADO1    LADO2    LADO3  AREA")
    print("*" * 50)
    print(f"{lado1} \t {lado2} \t {lado3} \t {area:.2f}") 
    
def leerNumero( etiqueta ):
    return float(input( etiqueta ))

'''def definirTriangulo():
    if lado1 == lado2 == lado3:
        mensaje = "EL TRIANGULO ES EQUILATERO"
    elif     '''


#ENTRADAS - BURBUJA LEER DATOS
#INICIO DE PROGRAMA

#libreria.limpiarPantalla() #Limpia la pantalla de Terminal
libreria.cabecera( "PROGRAMA ÁREA Y PERIMETRO TRIANGULO" )

#correr el programa N veces
continuar = True
while (continuar):
    #INVOCAMOS UNA FUNCIÓN QUE PERMITA LEER CUALQUIER NUMERO, CON DIFERENTE ETIQUETA
    lado1 = leerNumero( Fore.CYAN + "LADO 1: " + Style.RESET_ALL )
    lado2 = leerNumero( Fore.CYAN + "LADO 2: " + Style.RESET_ALL )
    lado3 = leerNumero( Fore.CYAN + "LADO 3: " + Style.RESET_ALL )


    if ((lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2)):
        #PROCESOS
        area = calcularArea( lado1, lado2, lado3 )
        perimetro = calcularPerimetro( lado1, lado2, lado3)  #invocar o llamar a la funcion

        #SALIDAS
        mostrarArea(lado1, lado2, lado3, area)   #llamado
        mostrarPerimetro(lado1, lado2, lado3, perimetro)   #llamado
    else:
        print("EL TRIANGULO NO SE PUEDE CONSTRUIR")
    
    respuesta = input("DESEA CONTINUAR (Si - No)")[0].lower()
    if (respuesta == 's'):
        continue
    else:
        break

print("FIN DEL PROGRAMA")