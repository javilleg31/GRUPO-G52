'''
INDICAR DE ACUERDO A LA EDAD DE UNA PERSONA SI ES APTO PARA VOTAR O NO
ANALISIS:
    ENTRADAS: edad
    PROCESOS: mensaje = "ES APTO PARA VOTAR"     ????  edad > 18
              mensaje = "NO ES APTO PARA VOTAR"  ????  edad < 18
    SALIDAS : mensaje
'''
def leerNumero( etiqueta ):
    return float(input( etiqueta ))


def definirSiEsApto ( edad ):
    if edad >= 18:
        mensaje = "ES APTO PARA VOTAR"
    else:
        mensaje = "NO ES APTO PARA VOTAR"
    return mensaje

def generarSalida (edad, mensaje):
    print("EDAD MENSAJE")
    print(f"{edad}  {mensaje} ")

#VARIABLES GLOBALES INICIALIZADAS
edad = 0
mensaje = ""

#ENTRADAS
edad = leerNumero ( "INGRESE EDAD: " )

#PROCESOS
mensaje = definirSiEsApto ( edad )

#GENERA SALIDAS
generarSalida (edad, mensaje)