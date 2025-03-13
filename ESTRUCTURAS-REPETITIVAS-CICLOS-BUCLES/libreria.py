

import os
import time
from colorama import Fore, Back, Style, init

init()

#La función devuelve el nombre del sistema operativo y aplica el comando respectivo
def limpiarPantalla ():    
    if os.name == 'nt':  # Para sistemas Windows
        os.system('cls')
    else:  # Para sistemas Unix/Linux/Mac
        os.system('clear')
    
def cabecera ( titulo ): 
    print(Fore.RED + f"\n   {titulo}    \n" + Style.RESET_ALL )

def validarEntero ( etiqueta, minimo, maximo=float("inf")):   #si no se envia el maximo queda al infinito
    while True:
        try:
            valor = int(input(etiqueta))
            if valor < minimo or valor > maximo:
                print (f"ERROR - EL NUMERO DE SER ENTRE {minimo} y {maximo}")
                continue
            return valor
        except ValueError:
            mensajeErrorEsperaSegundos( "ERROR - NUMERO NO VÁLIDO", 1 )

def validarFlotante ( etiqueta, minimo, maximo=float("inf")):   #si no se envia el maximo queda al infinito
    while True:
        try:
            valor = input(etiqueta).replace(",", ".")
            valor = float(valor)
            if valor < minimo or valor > maximo:
                print (f"ERROR - EL NUMERO DE SER ENTRE {minimo} y {maximo}")
                continue
            return valor
        except ValueError:
            mensajeErrorEsperaSegundos( "ERROR - NUMERO NO VÁLIDO", 1 )

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

