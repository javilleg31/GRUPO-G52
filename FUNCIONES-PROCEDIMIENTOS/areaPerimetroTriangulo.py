'''
Planteamiento de Problema: Desarrollar un programa en Lenguaje Python, que permita hallar el área y perímetro de cualquier triángulo, utilizando funciones, para las entradas, procesos y salidas:
Restricciones para calcular el área NO se requiere de la altura
perimetro = lado1 + lado2 + lado3
'''
import math
import libreria
#cuerpo o definicion de la funcion con retorno a donde fue llamado
def calcularPerimetro( lado1, lado2, lado3):
    return lado1 + lado2 + lado3

#cuerpo o definicion de la funcion con retorno a donde fue llamado
def calcularArea( lado1, lado2, lado3 ):
    semiperimetro = (lado1 + lado2 + lado3) / 2
    area = math.sqrt(semiperimetro * (semiperimetro - lado1) * (semiperimetro - lado2) * (semiperimetro - lado3))
    return area

#PROCEDIMIENTO
def mostrarPerimetro(lado1, lado2, lado3, perimetro):
    print("\n\n", "*" * 50)
    print(" LADO1    LADO2    LADO3  PERIMETRO")
    print("*" * 50)
    print(f"{lado1} \t {lado2} \t {lado3} \t {perimetro}") 

#PROCEDIMIENTO no retorna valor
def mostrarArea(lado1, lado2, lado3, area):
    print("\n\n", "*" * 50)
    print(" LADO1    LADO2    LADO3  AREA")
    print("*" * 50)
    print(f"{lado1} \t {lado2} \t {lado3} \t {area:.2f}") 

def leerNumero( etiqueta ):
    return float(input( etiqueta ))

libreria.limpiarPantalla() 

#ENTRADAS - BURBUJA LEER DATOS
'''
lado1 = float(input("LADO 1: "))
lado2 = float(input("LADO 2: "))
lado3 = float(input("LADO 3: "))
'''
#inicio del programa
os.system("cls")   #limpia la pantalla del terminal 

#INVOCAMOS UNA FUNCION QUE PERMITA LEER CUALQUIER NUMERO, CON DIFERENTE ETIQUETA
lado1 = leerNumero("LADO 1:")
lado2 = leerNumero("LADO 2:")
lado3 = leerNumero("LADO 3:")

#PROCESOS
area = calcularArea( lado1, lado2, lado3 )
perimetro = calcularPerimetro( lado1, lado2, lado3)  #invocar o llamar a la funcion

#SALIDAS
mostrarArea(lado1, lado2, lado3, area)   #llamado
mostrarPerimetro(lado1, lado2, lado3, perimetro)   #llamado



