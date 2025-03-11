'''
Programa que me permita pagar el salario de un empleado que devenga por horas.

ANALISIS: QUÉ
    ENTRADAS : horasTrabajadas, valorHora
    PROCESOS : pago = horasTrabajadas * valorHora
    SALIDAS  : pago
'''
cabecera( "PAGO DEL SALARIO INTEGRAL")
#[1]. IMPORTAR LIBRERIAS - PREDEFINIDAS DE PYTHON O PROPIAS

#[2]. DEFINIR FUNCIONES - PROCEDIMIENTOS - PROPIAS - REGRESA A DONDE FUE LLAMADO
#sumar = lambda x, y: x + y
calcularPago = lambda horasTrabajadas, valorHora : horasTrabajadas * valorHora

def mostrarPago ( horasTrabajadas, valorHora, pago ):
    print("*" * 50)
    print("HORAS LABORADAS  VALOR HORA   PAGO ")
    print("*" * 50)
    print(f"{horasTrabajadas} \t {valorHora} \t {pago}")

#[3]. VARIABLES GLOBALES
pago = 0

#[4]. ENTRADAS
horasTrabajadas = int(input("HORAS TRABAJADAS: "))
valorHora       = int(input("VALOR HORA: "))

#[5]. PROCESOS
#pago = horasTrabajadas * valorHora
pago = calcularPago( horasTrabajadas, valorHora )

#[6]. SALIDAS   con variables locales
mostrarPago ( horasTrabajadas, valorHora, pago )

