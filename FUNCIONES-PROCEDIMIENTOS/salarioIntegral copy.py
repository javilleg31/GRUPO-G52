'''
Programa que me permita pagar el salario de un empleado que devenga por horas.

ANALISIS: QUÉ
    ENTRADAS : horasTrabajadas, valorHora
    PROCESOS : pago = horasTrabajadas * valorHora
    SALIDAS  : pago
'''
import sys
import os

# Obtener la ruta absoluta del directorio GRUPO-G52
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Agregar la carpeta BIBLIOTECA al sys.path
sys.path.append(os.path.join(base_dir, "BIBLIOTECA"))
#print(sys.path)
# Importar libreria
import libreria

#[1]. IMPORTAR LIBRERIAS - PREDEFINIDAS DE PYTHON O PROPIAS
#import os
#import libreria

#[2]. DEFINIR FUNCIONES - PROCEDIMIENTOS - PROPIAS - REGRESA A DONDE FUE LLAMADO

def calcularPago( horasTrabajadas, valorHora ):
    return horasTrabajadas * valorHora

def mostrarPago ( horasTrabajadas, valorHora, pago ):
    print("*" * 50)
    print("HORAS LABORADAS  VALOR HORA   PAGO ")
    print("*" * 50)
    print(f"{horasTrabajadas} \t {valorHora} \t {pago}")


libreria.limpiarPantalla()   #invocando o llamando el procedimiento
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

