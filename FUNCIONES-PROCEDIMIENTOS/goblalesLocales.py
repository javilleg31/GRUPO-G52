x = 10      # Variable global 
print(f"X INICIANDO: {x}")
# Definimos o construimos la estructura de la función que va ser invocada o llamada
def modificar_global() :
	global   x     # Declarar que vamos a usar la variable global x 
	x = 20         # Modificar la variable global 


modificar_global()       # Invocamos la función que debe existir antes de ser llamada

print(f"X AL FINAL: {x}")     # Imprime 20 
