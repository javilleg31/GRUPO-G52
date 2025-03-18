'''
Desarrollar un programa en Lenguaje Python, que permita hallar 
el área de un triángulo

ANALISIS: R - D - S
    ENTRADAS - QUE ME DAN - QUE NECESITO:       base, altura                INPUT
    PROCESOS - FORMULAS :     areaTriangulo <-- base * altura / 2           ? = ? ? ?
    SALIDAS  - QUE ME PIDEN:  areaTriangulo                                 PRINT
'''
#importar mi biblioteca
import os
import sys

# Obtener la ruta absoluta de la carpeta raíz del proyecto (PROYECTO) 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Agregar la carpeta BIBLIOTECA al path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
# Importar libreria
import libreria   #la primera vez muestra error de sintaxis


#PROGRAMA

#1. ENTRADAS
base   = libreria.leerFlotante ( "BASE: ",   1, 100)       #float(input("INGRESE BASE: "))
altura = libreria.leerFlotante ( "ALTURA: ", 1, 20   )#float(input("INGRESE ALTURA: "))
tipoTriangulo = libreria.LeerCaracter ("TIPO TRIANGULO [I]Isosceles [E]Equilatero [S]Escaleno: ")
#tipoTriangulo = tipoTriangulo.lower()
#2. PROCESOS
areaTriangulo = base * altura / 2    # 10 * 5 / 2    =>  50 / 2  => 25

#3. SALIDAS
#print( areaTriangulo )
print(f" {base}  * {altura} / 2 = {areaTriangulo:.2f}")

