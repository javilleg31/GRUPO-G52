#todo programa debe ser controlado por un MENU, con opciones de INGRESAR Y MOSTRAR Y SALIR
#importar mi biblioteca
import os
import sys
import time

# Obtener la ruta absoluta de la carpeta raíz del proyecto (PROYECTO) 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Agregar la carpeta BIBLIOTECA al path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
# Importar libreria
import libreria   #la primera vez muestra error de sintaxis

#dibujar el menu
def menu ():
    libreria.limpiarPantalla()
    print("*** MENU PRINCIPAL ***")
    print("[1]. INSERTAR")
    print("[2]. LISTAR")
    print("[3]. CONSULTAR")
    print("[4]. ACTUALIZAR")
    print("[5]. ELIMINAR")
    print("[6]. SALIR")

#INICIO DEL PROGRAMA
while True:
    menu ()
    #opcion = input("OPCION: ")[0]
    opcion = libreria.LeerCaracter("OPCION: ")
    match opcion:
        case '1':
            print("LLAMADO A LA FUNCION INSERTAR") #insertar()
            time.sleep(2)
        case '2':
            print("LLAMADO A LA FUNCION LISTAR")    #listar()
            time.sleep(2)
        case '3':
            print("LLAMADO A LA FUNCION CONSULTAR") #consultar()
            time.sleep(2)
        case '4':
            print("LLAMADO A LA FUNCION ACTUALIZAR") #actualizar()
            time.sleep(2)
        case '5':
            print("LLAMADO A LA FUNCION ELIMINAR") #eliminar()
            time.sleep(2)
        case '6':
            print("SALE DEL PROGRAMA ") #insertar()
            time.sleep(2)
            break
        case _:
            print("OPCION NO VALIDA") #eliminar()
            time.sleep(2)
            libreria.limpiarPantalla()


