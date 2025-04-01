import matplotlib.pyplot as linea

# Datos
etiquetas = ['Programación', 'Inglés', 'Proyectos', 'Habilidades']  #EJE X
valores = [4.5, 3, 5, 4]      #EJE Y

# Crear el gráfico de líneas
linea.plot(etiquetas, valores, marker='o')   #CONFIGURAR LA GRAFICA CON SUS VALORES

# Añadir los valores en los puntos de quiebre
for i, valor in enumerate(valores):
    linea.text(i, valor + 0.1, str(valor), ha='center')

# Añadir títulos y etiquetas
linea.xlabel('Componentes')   #Leyendas para el eje X
linea.ylabel('Promedios')     #valores para el eje Y
linea.title('Promedios x Componentes')  #titulo de la gráfica

# Mostrar el gráfico
linea.show()
