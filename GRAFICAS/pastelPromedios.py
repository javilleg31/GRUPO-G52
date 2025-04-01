
#PASTEL O TORTA
import matplotlib.pyplot as pastel

# Datos de ejemplo
labels = ['Programación', 'Inglés', 'Proyectos', 'Habilidades']
sizes = [4.5, 3, 5, 4]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # solo "explota" el primer pedazo

# Crear la gráfica de pastel
pastel.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

pastel.axis('equal')  # Asegura que el pastel se dibuje como un círculo

# Añadir título
pastel.title('PROMEDIOS X COMPONENTES - TALENTO TECH')

# Mostrar la gráfica
pastel.show()
