'''
Desarrollar un programa en python, que permita hallar la definitiva de una materia que cursa un estudiante
sabiendo que: primer parcial es el 20%  el segundo parcial 30% y un final que equivale al resto de

ADICIONAL: INDICAR CON UN MENSAJE SI APRUEBA O REPRUEBA EL CURSO

ENTRADAS - QUE ME DAN, QUE NECESITO    : PERIFERICO EL TECLADO
    PROCESOS : CPU - ALU - UNIDAD ARIMETICA
    SALIDAS - QUE ME PIDEN - QUE MUESTRO  : PANTALLA

ANALISIS: EL QUÉ  primer_parcial
    ENTRADAS : nombreEstudiante, nombreMateria, primerParcial, segundoParcial, final
    PROCESOS : definitiva = primerParcial * 20% + segundoParcial * 30% + final * 50%
    SALIDAS  : definitiva
               mensaje      ?????  definitiva < 3
'''
#PROGRAMA EN PYTHON PARA INTERACTURA CON EL USUARIO FINAL - CLIENTE
#[1]. IMPORTAR LIBRERIAS PREDEFINIDAS

#[2]. DEFINICION O CUERPO FUNCIONES PROPIAS
def leerCadena ( etiqueta ):
    return input( etiqueta )

def leerNumero( etiqueta ):
    return float(input( etiqueta ))

def calcularDefinitiva( primerParcial, segundoParcial, final):
    return primerParcial * PORCENTAJE1 + segundoParcial * PORCENTAJE2 + final * PORCENTAJE3

#PROCEDIMIENTO NO RETORNA VALOR
def mostrarSalida (nombreEstudiante, nombreMateria, definitiva, mensaje):
    print(f"ESTUDIANTE: {nombreEstudiante} ASIGNATURA: {nombreMateria} DEFINITIVA: {definitiva:.2f} {mensaje}" )
#[3]. CONSTANTES Y VARIABLES GLOBALES INICIALIZADAS
PORCENTAJE1 = 20 / 100
PORCENTAJE2 = 0.30
PORCENTAJE3 = 50 / 100

primerParcial  = 0
segundoParcial = 0
final          = 0
definitiva     = 0

#[4]. ENTRADAS - CON FUNCIONES
nombreEstudiante = leerCadena( "NOMBRE ESTUDIANTE: " )   #INVOCAR O LLAMAR LA FUNCION
nombreMateria    = leerCadena( "NOMBRE MATERIA: " )

primerParcial    = leerNumero( "PRIMER PARCIAL: ")       #INVOCAR O LLAMAR LA FUNCION
segundoParcial   = leerNumero( "SEGUNDO PARCIAL: ")
final            = leerNumero( "FINAL: ")

#[5]. PROCESOS
definitiva = calcularDefinitiva( primerParcial, segundoParcial, final)
mensaje = "APRUEBA"
if (definitiva < 3):
    mensaje = "REPROBADO"

#[6]. SALIDAS
mostrarSalida( nombreEstudiante, nombreMateria, definitiva, mensaje )



