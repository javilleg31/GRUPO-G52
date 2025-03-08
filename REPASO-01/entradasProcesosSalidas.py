'''
Desarrollar un programa en python, que permita hallar la definitiva de una materia que cursa un estudiante
sabiendo que: primer parcial es el 20%  el segundo parcial 30% y un final que equivale al resto de

ENTRADAS - QUE ME DAN, QUE NECESITO    : PERIFERICO EL TECLADO
    PROCESOS : CPU - ALU - UNIDAD ARIMETICA
    SALIDAS - QUE ME PIDEN - QUE MUESTRO  : PANTALLA

ANALISIS: EL QUÉ  primer_parcial
    ENTRADAS : nombreEstudiante, nombreMateria, primerParcial, segundoParcial, final
    PROCESOS : definitiva = primerParcial * 20% + segundoParcial * 30% + final * 50%
    SALIDAS  : definitiva
'''
#PROGRAMA EN PYTHON PARA INTERACTURA CON EL USUARIO FINAL - CLIENTE
#[1]. IMPORTAR LIBRERIAS PREDEFINIDAS

#[2]. FUNCIONES PROPIAS

#[3]. CONSTANTES Y VARIABLES GLOBALES INICIALIZADAS
PORCENTAJE1 = 20 / 100
PORCENTAJE2 = 0.30
PORCENTAJE3 = 50 / 100

primerParcial  = 0
segundoParcial = 0
final          = 0
definitiva    = 0

#[4]. ENTRADAS
nombreEstudiante = input("NOMBRE ESTUDIANTE   : ")
nombreMateria    = input("NOMBRE MATERIA      : ")
primerParcial    = float(input("PRIMER PARCIAL: "))
segundoParcial   = float(input("SEGUNDO PARCIAL: "))
final            = float(input("FINAL PARCIAL: "))

#[5]. PROCESOS
definitiva = primerParcial * PORCENTAJE1 + segundoParcial * PORCENTAJE2 + final * PORCENTAJE3

#[6]. SALIDAS
print(f"ESTUDIANTE: {nombreEstudiante} ASIGNATURA: {nombreMateria} DEFINITIVA: {definitiva:.2f}" )


