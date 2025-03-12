

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

def mensajeEsperaSegundos( mensaje, segundos ):
    print(Fore.YELLOW + Style.BRIGHT + mensaje + Style.RESET_ALL)
    time.sleep( segundos )

##################################################################
# Procedimiento que espera que el usuario presione Enter         #
##################################################################
def mensajeEsperaEnter( mensaje ):
    print("\n" + Fore.GREEN + Style.BRIGHT + mensaje + Style.RESET_ALL, end="")
    input()

