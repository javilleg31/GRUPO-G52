import os
import time
from colorama import Fore, Back, Style, init

init()

import time 
import msvcrt

#función lee un solo carácter NO espera ENTER
def LeerCaracter (mensaje):
  print(mensaje, end="", flush=True)
  return msvcrt.getch().lower().decode('utf-8')  #getch captura un solo caracter No hay que dar enter


def  leerFlotante (mensaje, minimo, maximo):
  while True:
    print(f"{mensaje} ({minimo}-{maximo}): ", end="", flush=True)
    valor = input().strip().replace(",", ".")
    # Verificar que no esté vacío ni tenga espacios intermedios
    if not valor or " " in valor:
      print(f"Error: {mensaje} no debe estar vacío ni contener espacios.", end="", flush=True)
      time.sleep(1)              # Pausa breve de 1 segundo)
      print("\r\033[K", end="")  # \r Mueve cursor al inicio de la línea y limpia la línea con \033[K
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
      continue
    # Verificar si es un número decimal válido
    try:
      numero = float(valor)
      if minimo <= numero <= maximo:  # numero >= minimo and numero <= maximo
        return numero
      else:
        print(f"Error: {mensaje} debe estar entre {minimo} y {maximo}.", end="", flush=True)
        time.sleep(1) # Pausa breve de 1 segundo
        print("\r\033[K", end="")       # Mueve cursor al inicio de la línea y limpia la línea
        print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea
    except ValueError:
      print("Error: {mensaje} inválida. ", end="", flush=True)
      time.sleep(1)                      # Pausa breve de 1 segundo
      print("\r\033[K", end="")       # Mueve cursor al inicio de la línea y limpia la línea
      print("\033[F\033[K", end="") # Mueve cursor al final de la línea de arriba y limpia la línea

#La función devuelve el nombre del sistema operativo y aplica el comando respectivo
def limpiarPantalla ():    
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')
    
def cabecera ( titulo ): 
    print(Fore.RED + f"\n   {titulo}    \n" + Style.RESET_ALL )



def mensajeEsperaSegundos( mensaje, segundos ):
    print(Fore.YELLOW + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

def mensajeErrorEsperaSegundos( mensaje, segundos ):
    print(Fore.RED + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

##################################################################
# Procedimiento que espera que el usuario presione Enter         #
##################################################################
def mensajeEsperaEnter( mensaje ):
    print("\n" + Fore.GREEN + Style.BRIGHT + mensaje + Style.RESET_ALL, end="")
    input()

