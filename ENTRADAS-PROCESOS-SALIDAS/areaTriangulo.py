'''
Desarrollar un programa en Lenguaje Python, que permita hallar 
el área de un triángulo

ANALISIS: R - D - S
    ENTRADAS - QUE ME DAN - QUE NECESITO:       base, altura                INPUT
    PROCESOS - FORMULAS :     areaTriangulo <-- base * altura / 2           ? = ? ? ?
    SALIDAS  - QUE ME PIDEN:  areaTriangulo                                 PRINT
'''
#PROGRAMA

#1. ENTRADAS
base   = float(input("INGRESE BASE: "))
altura = float(input("INGRESE ALTURA: "))

#2. PROCESOS
areaTriangulo = base * altura / 2    # 10 * 5 / 2    =>  50 / 2  => 25

#3. SALIDAS
#print( areaTriangulo )
print(f" {base}  * {altura} / 2 = {areaTriangulo:.2f}")

