'''
ANALISIS:
    ENTRADAS: colorEspanyol
    PROCESOS: colorIngles = "YELLOW"
              colorIngles = "BLUE"
              colorIngles = "ROJO"
              colorIngles = "GREEN"
    SALIDAS : colorIngles
'''

def traducirColor( colorEspanyol ):
    match colorEspanyol:
        case "amarillo":
            colorIngles = "YELLOW"
        case "azul":
            colorIngles = "BLUE"
        case "rojo":
            colorIngles = "RED"
        case "verde":
            colorIngles = "GREEN"
        case _:
            colorIngles = "COLOR NO EXISTE"
    
    return colorIngles

#VARIALBLES GLOBALES
colorEspanyol = ""
#ENTRADAS
colorEspanyol = input("COLOR EN ESPAÑOL").lower()

#PROCESOS
colorIngles = traducirColor( colorEspanyol )

#SALIDAS
print(f"COLOR ESPAÑOL: {colorEspanyol}  COLOR INGLES: {colorIngles}")