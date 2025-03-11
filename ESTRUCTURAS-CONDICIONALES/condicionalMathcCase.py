'''
LEER UN MES EN NUMERO E INDICAR CON PALABRAS A CUAL CORRESPONDE, POR EJEMPLO 1 ES ENERO, 12 DICIEMBRE

ANALISIS:
    ENTRADAS: mes
    PROCESOS: nombreMes = "Enero"      ???  mes == 1 

              nombreMes = "Diciembre"  ???  mes == 12
    SALIDAS : nombreMes
'''
def generarSalida (mes, nombreMes):
    print("MES  NOMBRE")
    print(f"{mes}  {nombreMes} ")

def leerNumero( etiqueta ):
    return float(input( etiqueta ))

def encontrarNombreMes ( mes ):
    match ( mes ):
        case 1: 
            nombreMes = "ENERO"
        
        case 2: 
            nombreMes = "FEBRERO"
        
        case 12: 
            nombreMes = "DICIEMBRE"
        
        
        case _: 
            nombreMes = "MES NO EXISTE EN LA TIERRA"
    
    return nombreMes

#VARIABLES GLOBALES INICIALIZADAS

#ENTRADAS
mes = leerNumero ( "MES EN NUMERO: " )

#PROCESOS
nombreMes = encontrarNombreMes ( mes )

#GENERA SALIDAS
generarSalida (mes, nombreMes)

