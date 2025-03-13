'''
PREGUNTAR la edad de varias personas hasta que se ingrese una edad negativa
hallar el promedio de edades

ANALISIS:
    ENTRADAS:   edad
    PROCESOS:   sumaEdades = sumaEdades + edad
                cantidadEdades = cantidadEdades + 1
                promedio = sumaEdades / cantidadEdades
    SALIDAS:  promedio
'''

#inicializar varialbes
edad = 0
sumaEdades = 0
cantidadEdades = 0
promedio = 0

#ENTRADAS
while True:    
    edad = int(input("EDAD (NEGATIVA PARA SALIR): "))
    if (edad <= 0):
        break
    #procesos
    cantidadEdades = cantidadEdades + 1
    sumaEdades     = sumaEdades + edad    #tiempo parcila

promedio = sumaEdades / cantidadEdades   #salida ent timpo total

print(f"CANTIDAD EDADES: {cantidadEdades} SUMA={sumaEdades} \t PROMEDIO: {promedio}")
