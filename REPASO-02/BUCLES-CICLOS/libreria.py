#contiene funciones, procedimients propios, para ser reutilizados desde otros de mis programas

def leerFlotante ( etiqueta ):
    return float(input( etiqueta ))

def leerCadena( etiqueta ):
    return  input(etiqueta).capitalize()

def leerCaracter( etiqueta ):
    return  input(etiqueta)[0].strip().upper()


