

import os
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
