#HISTOGRAMAS
import matplotlib.pyplot as histograma

# Datos
etiquetas = ['Programación', 'Inglés', 'Proyectos', 'Habilidades']
valores = [4.5, 3, 5, 4]

# Crear el histograma
histograma.bar(etiquetas, valores)

# Añadir los valores encima de las barras
for i, valor in enumerate(valores):
    histograma.text(i, valor + 0.1, str(valor), ha='center')

# Añadir títulos y etiquetas
histograma.xlabel('Componentes')
histograma.ylabel('Promedios')
histograma.title('Promedios x Componentes')

# Mostrar el gráfico
histograma.show()
