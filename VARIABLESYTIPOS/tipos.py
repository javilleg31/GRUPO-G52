#PROBLEMA PLANTEADO - ASIGNAR VALORES A LAS VARIABLES QUE CORRESPONDAN A LOS DATOS PERSONALES DE ALGUIEN
#VARIABLES PRIMITIVAS

#STR  STRING O CADENA de texto
nombreCompleto = "MARIANA RESTREPO"   #EL VALOR ES ASIGNADO A UNA VARIABLE - en la R.A.M.
print("EL NOMBRE ALMACENADO ES: " + nombreCompleto )    #PRINT mostrar en pantalla sin formato

#STR cadena de caracter
genero = 'M'

#INT numericos sin decimales
edad = 23

#FLOAT numericos con decimales
estatura = 1.72   #los decimales son con punto NO con coma

print ("\n\n*****************************************")
print ("NOMBRRE  \t GÉNERO  EDAD     ESTATURA")
print ("*" * 60)
print(f"{nombreCompleto}   {genero} \t\t {edad}   {estatura}")   #salida con formato f y {variables}

#identificar el tipo de dato de una variable
print("ESTATURA ES DE TIPO: ", type(estatura))
print("NOMBRE ES DE TIPO: ",   type(nombreCompleto))
print("EDAD ES DE TIPO: ",     type(edad))

#salida masiva
print("NOMBRE: ", nombreCompleto, "EDAD: ", edad, "ESTATURA: " + str(estatura) )

#NUMERICOS ENTEROS
