#una lista se utiliza para agrupar cada una de las entidades(persona, lugar, objeto..) de un problema

from tabulate import tabulate
from colorama import Fore, Back, Style, init

init()

encabezado = [Fore.GREEN + Style.BRIGHT + "ID", "Nombre", "Programación", "Inglés", "Habilidades" + Style.RESET_ALL]

estudiantes = [
  [101, "Juan Pérez", 4.0, 3.5, 2.8],   #indice 0
  [102, "Ana Gómez", 2.9, 3.8, 3.0]     #indice 1
]

'''
idientificacion = input("identificacion:")
nombre = input("Nombre)

nota3 = float(input("NOTA 2: ))

estudiante = [identificacion, nombre, nota1, nota2, nota3]  #lista simple para una sola entidad
estudiantes.append(estudiante)                   #lista de listas almacenar todas las entidades
guardar(estudiantes) #volcado a un archivo binario
'''

print(estudiantes)

headers =   encabezado; #dependiendo de la entidad, se envian por parametro
print(tabulate(estudiantes,
         headers = headers,
         tablefmt='fancy_grid',
         stralign='left',
         floatfmt=",.1f"))