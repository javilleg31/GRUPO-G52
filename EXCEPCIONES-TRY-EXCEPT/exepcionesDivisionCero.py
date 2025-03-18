
#INICIALIZAR VARIABLES
dividendo = 10
divisor = 0
resultado = 0
#resultado = dividendo / divisor
try:
    resultado = dividendo / divisor
except ZeroDivisionError:
    print("LA DIVISION POR CERO TODAVIA NO EXISTE")

print(resultado)