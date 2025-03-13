'''
HALLAR EL PROMEDIO DE TRES NOTAS, de un estudiante
ANALISIS  R                                  D                      S
    QUE ME DAN - QUE NECESITO  <=> ENTRADAS: nota1, nota2, nota3
    FORMULAS                   <=> PROCESOS: promedio = (nota1 + nota2 + nota3) / 3
    QUE ME PIDEN - QUE MUESTRO <=> SALIDAS : promedio
'''

#P  EL PROGRAMA
#[1].  VARIABLES INICIALIZADAS EN UN VALOR DE ACUERDO AL TIPO
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
promedio = 0.0
nombreEstudiante = ""

#[2]. ENTRADAS 
nombreEstudiante = input("ESTUDIANTE: ")
nota1 = float(input("NOTA 1:"))
nota2 = float(input("NOTA 2:"))
nota3 = float(input("NOTA 3:"))

#[3]. PROCESOS O FORMULAS
promedio = (nota1 + nota2 + nota3) / 3

#[4]. SALIDAS
print("ESTUDIANTE NOTA1 NOTA2 NOTA3 PROMEDIO")
print("_" * 40)
#print(nombreEstudiante, '\t', nota1,'\t', nota2, '\t', nota3, '\t', promedio)
print(f"{nombreEstudiante} \t {nota1} \t {nota2} \t {nota3} \t {promedio:.2f}")