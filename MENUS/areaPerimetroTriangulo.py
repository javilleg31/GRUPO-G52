'''
Planteamiento de Problema: Desarrollar un programa en Lenguaje Python, que permita hallar el área y perímetro de cualquier triángulo, utilizando funciones, para las entradas, procesos y salidas:
Restricciones para calcular el área NO se requiere de la altura
perimetro = lado1 + lado2 + lado3
'''
import math
#todo programa debe ser controlado por un MENU, con opciones de INGRESAR Y MOSTRAR Y SALIR
#importar mi biblioteca
import os
import sys
import time

# Obtener la ruta absoluta de la carpeta raíz del proyecto (PROYECTO) 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Agregar la carpeta BIBLIOTECA al path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
# Importar libreria
import libreria   #la primera vez muestra error de sintaxis


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

#ENTRADAS - BURBUJA LEER DATOS
#inicio del programa
libreria.limpiarPantalla()   #limpia la pantalla del terminal 
libreria.cabecera( "PROGRAMA AREA Y PERIMETRO DEL TRIANGULO")

#dibujar el menu
def menu ():
    libreria.limpiarPantalla()
    print("*** MENU PRINCIPAL - TRIANGULOS***")
    print("[1]. DATOS DEL TRIANGULO")
    print("[2]. LISTAR")
    print("[3]. SALIR")

#INICIO DEL PROGRAMA
while True:
    menu ()
    #opcion = input("OPCION: ")[0].lower()
    opcion = libreria.LeerCaracter("OPCION: ")
    match opcion:
        case '1':
            #INVOCAMOS UNA FUNCION QUE PERMITA LEER CUALQUIER NUMERO, CON DIFERENTE ETIQUETA
            lado1 = libreria.leerFlotante("LADO 1: ", 1, 1000)
            lado2 = libreria.leerFlotante("LADO 2: ", 1, 1000)
            lado3 = libreria.leerFlotante("LADO 3: ", 1, 1000)     
            #LADO1, LADO2, LADO3 = leerDatos ()   #return LADO1, LADO2, LADO3
            #PROCESOS
            area = calcularArea( lado1, lado2, lado3 )
            perimetro = calcularPerimetro( lado1, lado2, lado3)  #invocar o llamar a la funcion               
            
        case '2':
            #SALIDAS
            mostrarArea(lado1, lado2, lado3, area)   #llamado
            mostrarPerimetro(lado1, lado2, lado3, perimetro)   #llamado 
            libreria.limpiarPantalla()           
            libreria.mensajeEsperaEnter( "PRESIONE <ENTER> PARA CONTINUAR" )
        case '3':
            print("SALE DEL PROGRAMA ") #insertar()
            time.sleep(2)
            break
        case _:
            print("OPCION NO VALIDA") #eliminar()
            time.sleep(2)
            libreria.limpiarPantalla()



