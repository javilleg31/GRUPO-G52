'''
HALLAR EL PROMEDIO DE TRES NOTAS, de un estudiante, 
e indicar si aprueba (mayor a 3), reprueba(menor 2), habilita(entre 2 y 3)
mostrar el genero de la persona HOMBRE-MUJER-OTRO

ANALISIS  R                                  D                      S
    ENTRADAS: nombreEstudiante, genero, nota1, nota2, nota3
    PROCESOS: promedio = (nota1 + nota2 + nota3) / 3
    SALIDAS : promedio, genero
              estadoAprobacion  <=> "APRUEBA, REPUESTBA O HABILITA" ??? DEPENDE DEL PROMEDIO
'''
import libreria

#DEFINICION O CUERPO O CONSTRUCJCION DE FUNCIONES PROPIAS
def calcularPromedio ( nota1, nota2, nota3 ):    
    #pueden haber mas instrucciones
    return (nota1 + nota2 + nota3) / 3

def traerEstado (promedio):
    if (promedio >= 3):
        estadoAprobacion = "APROBADO"
    elif (promedio < 2):
        estadoAprobacion = "REPROBADO"
    else:
        estadoAprobacion = "HABILITA"
    return estadoAprobacion

def traerNombreGenero (genero):
    match (genero):
        case 'M': generoLetras="Másculino"
        case 'F': generoLetras="Femenino"
        case 'O': generoLetras="Otro"
        case _: generoLetras="No Definido"
    return generoLetras

#PROCEDIMIENTO - NO RETORNA NINGUN VALOR
def generarSalidas (nombreEstudiante, genero, nota1, nota2, nota3, promedio, estadoAprobacion):
    print("ESTUDIANTE NOTA1 NOTA2 NOTA3 PROMEDIO")
    print("_" * 40)
    #print(nombreEstudiante, '\t', nota1,'\t', nota2, '\t', nota3, '\t', promedio)
    print(f"{nombreEstudiante} \t {genero} \t {nota1} \t {nota2} \t {nota3} \t {promedio:.2f} \t {estadoAprobacion}")


#P  EL PROGRAMA
#[1].  VARIABLES INICIALIZADAS EN UN VALOR DE ACUERDO AL TIPO
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
promedio = 0.0
nombreEstudiante = ""
estadoAprobacion = ""
genero = ''

#[2]. ENTRADAS 
nombreEstudiante = libreria.leerCadena ( "NOMBRE: ") #nombreEstudiante = input("ESTUDIANTE: ")
genero           = libreria.leerCaracter ( "GENERO ([M]Másculino [F]Femenino [O]Otro): ") #genero un solo caracter")
nota1 = libreria.leerFlotante( "NOTA 1 (0..5): " )         #nota1 = float(input("NOTA 1:"))
nota2 = libreria.leerFlotante( "NOTA 2 (0..5): " )         #nota2 = float(input("NOTA 2:"))
nota3 = libreria.leerFlotante( "NOTA 3 (0..5): " )         #nota3 = float(input("NOTA 3:"))

#[3]. PROCESOS O FORMULAS
#promedio = (nota1 + nota2 + nota3) / 3
promedio = calcularPromedio ( nota1, nota2, nota3 )  #invocamos o llamamos la funcion

estadoAprobacion = traerEstado (promedio)
generoLetras = traerNombreGenero (genero)
#[4]. SALIDAS - PROCEDIMIENTOS
generarSalidas (nombreEstudiante, generoLetras, nota1, nota2, nota3, promedio, estadoAprobacion)

