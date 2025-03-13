'''
Programa que permita mostrar la conocida serie de FIBONACCI, crear un función que la invoque y la muestre, por ejemplo: myFibbonacci (n).
La siguiente es la serie FIBONACCI “0 - 1 – 1  – 2 – 3 – 5 – 8 – 13. – 21 …….”
                                   ant act  r
Hallar la sumatoria de los todos los números de la serie
La serie finaliza cuando la sumatoria sobrepase el valor de 1000
NO utilizar el método de la biblioteca Python fibbo(), crear su propia función

ANALISIS:
    ENTRADAS:
    PROCESOS: sumatoria = sumatoria + ?  suma de cada termino
    SALIDAS : serie, sumatoria
'''

SUMA_FINAL = 1000
anterior = 0
actual = 1
sumatoria = 0
print(f"{anterior} - {actual}")
while (sumatoria  < SUMA_FINAL):
    resultado = anterior + actual
    print(f" - {resultado}", end="")
    sumatoria = sumatoria + resultado
    anterior = actual
    actual = resultado


