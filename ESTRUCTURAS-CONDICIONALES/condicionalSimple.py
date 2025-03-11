'''
incrementar el salario de un empleado, con su subsidio de transporte
ANALISIS: 
    ENTRADAS: salario
    PROCESOS: subsidio = ??? salario <= dos*Minimos
              pago = salario + subsidio
    SALIDAS : pago

'''
#[1]. IMPORTAR LIBRERIAS PREDEFINIDAS COMO MATH

#[2]. FUNCIONES PROPIAS O PERSONLIZADAS
def leerNumero( etiqueta ):
    return float(input( etiqueta ))

def calcularPago ( salario, subsidioTransporte):
    return salario + subsidioEmpleado

def mostrarResultados( salario, subsidioEmpleado, pago ):
    print("SALARIO    TRANSPORTE    PAGO")
    print(f"{salario}  {subsidioEmpleado}  {pago}")

#[3]. CONSTANTES
SUBSIDIO_TRANSPORTE = 200000
MINIMO   = 1400000

#[4]. VARIABLES GLOBALES INICIALIZADAS
salario = 0
pago = 0

#[5]. ENTRADAS - FUNCIONES
salario = leerNumero( " INGRESE SALARIO: " )

#[6]. PROCESOS - FUNCIONES
subsidioEmpleado = 0    #INICIALMENTE TODO MUNDO TIEN0 PESOS
if (salario <= (2 * MINIMO)):    #SI GANA MENOS DE DOS MINIMOS LE PAGAMOS SUBSIDIO
    subsidioEmpleado = SUBSIDIO_TRANSPORTE

pago = calcularPago (salario, subsidioEmpleado )

#[7]. SALIDAS - PROCEDIMIENTOS
mostrarResultados( salario, subsidioEmpleado, pago )