import pandas as tabla
import numpy as np
import dateutil

# Crear un DataFrame de ejemplo
data = [
    ['COMP001', 'Programación', 20, 4.5],
    ['COMP002', 'Inglés', 23, 3],
    ['COMP003', 'Proyecto', 19, 5],
    ['COMP004', 'Habilidades', 21, 4]
]
column_names = ['CODIGO', 'COMPONENTE', 'CANTIDAD ESTUDIANTES', 'NOTA PROMEDIO']
tablaPromedio = tabla.DataFrame(data, columns=column_names)

print(tablaPromedio)
