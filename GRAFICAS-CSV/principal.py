

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def leer_archivo(archivo):
    try:
        return pd.read_csv(archivo)  #carga los datos en un DataFrame
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def graficar_lineas(datos, columna_pais, columna_produccion, columna_consumo):
    
    datos.groupby(columna_pais)[columna_produccion].sum().plot(kind='line', color='blue', label='Producción')
    datos.groupby(columna_pais)[columna_consumo].sum().plot(kind='line', color='green', label='Consumo')
	
    plt.title('Producción y Consumo de Energía por País')
    plt.xlabel('Paises')
    plt.ylabel('valores en KW')
    plt.legend()  #recuadro explicativo x color y categoria
	
    plt.show()

def graficar_pastel(datos, columna_pais, columna_produccion, columna_consumo):
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    
    datos.groupby(columna_pais)[columna_produccion].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax[0])
    ax[0].set_title('Producción de Energía')
    ax[0].set_ylabel('')
    
    datos.groupby(columna_pais)[columna_consumo].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax[1])
    ax[1].set_title('Consumo de Energía')
    ax[1].set_ylabel('')
    
    plt.show()

def graficar_histograma_agrupado(datos, columna_pais, columna_produccion, columna_consumo):  
  # Agrupar datos por país y calcular los totales
  produccion = datos.groupby(columna_pais)[columna_produccion].sum()
  consumo    = datos.groupby(columna_pais)[columna_consumo].sum()
  # Crear el gráfico
  paises = produccion.index
  x = np.arange(len(paises)) # Posiciones en el eje X
  ancho = 0.35 # Ancho de cada barra
  fig, ax = plt.subplots(figsize=(10, 6))

  # Barras para producción y consumo
  barras1 = ax.bar(x - ancho/2, produccion, width=ancho, label="Producción", color='skyblue', edgecolor='black')
  barras2 = ax.bar(x + ancho/2, consumo, width=ancho, label="Consumo", color='lightgreen', edgecolor='black')  # Colocar valores encima de las barras de producción
  
  for barra in barras1:
    ax.annotate(f'{barra.get_height():.0f}', 
          (barra.get_x() + barra.get_width() / 2, barra.get_height()), 
          ha='center', va='bottom')
     
     # Colocar valores encima de las barras de consumo
  for barra in barras2:
    ax.annotate(f'{barra.get_height():.0f}', 
          (barra.get_x() + barra.get_width() / 2, barra.get_height()), 
          ha='center', va='bottom')
       
  # Personalización del gráfico
  ax.set_xlabel("Paises")
  ax.set_ylabel("Total Kw")
  ax.set_title("Producción y Consumo de Energía por País")
  ax.set_xticks( x )
  ax.set_xticklabels(paises, rotation=45)
  ax.legend()
  ax.grid(axis='y', linestyle='--', alpha=0.7)

  # Mostrar el gráfico
  plt.tight_layout()
  plt.show()

def menu():
    archivo = input("\n\nIngresa el nombre del archivo (con extensión .csv): ")  #nombrecarpeta/nombrearchivo.csv
    datos = leer_archivo(archivo)    #datos e un DataFrame
    if datos is not None:
        while True:
            print("\nMenú de Gráficas")
            print("1. Gráfico de Pastel")
            print("2. Histograma")
            print("3. Gráfico de Líneas")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                graficar_pastel(datos, 'País', 'Producción', 'Consumo')
            elif opcion == '2':
                graficar_histograma_agrupado(datos, 'País', 'Producción', 'Consumo')
            elif opcion == '3':
                graficar_lineas(datos, 'País', 'Producción', 'Consumo')
            elif opcion == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
