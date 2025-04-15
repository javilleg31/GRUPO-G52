#importar los modulos necesarios de flask y otros
from flask import Flask, render_template, request, jsonify
import pickle #para guardar y cargar datos del archivo binario
import os #para verificar si el archivo existe

#crea l ainstancia de la aplicación Flask, para comunicación de datos - entre cliente y servidor
app = Flask(__name__)

def guardar_datos ( lista ):
    with open(ARCHIVO, 'wb') as f:
        return pickle.dump(lista, f)

def cargar_datos ():
    if (os.path.exists(ARCHIVO)):  #verifica si existe el archivo
        with open(ARCHIVO, 'rb') as f:
            return pickle.load(f)  #carga la lista desde el archivo
    return []  #si no existe el archivo, inicie una lista vacia


ARCHIVO = 'datos/personas.dat'

#DICCIONARIOS PARA CARGAR EN LOS COMBOS
CIUDADES = {
    '01': 'Armenia',
    '02': 'Risaralda',
    '03': 'Manizales',
    '04': 'Medellín'
}

GENEROS = {
    'M': 'Máculino',
    'F': 'Femenino',
    'O': 'Otro',
}

#FUNCIONES DE FLASK PARA EL CRUD
@app.route('/')
def index():
    #carga el archiovo html llamado index, y lo muestra en el navegador
    return render_template('index.html')

@app.route('/generos')
def get_generos():
    return jsonify(GENEROS)

@app.route('/ciudades')
def get_ciudades():
    return jsonify(CIUDADES)

#OPERACIONES DE CRUD - INSERTAR
@app.route('/persona', methods=['POST'])
def insertar ():
    data = request.json   #obtiene los datos enviados desde el front end en formato json
    personas = cargar_datos()  #cargamos en la lista desde el archivo

    #validar duplicados
    for p in personas:
        if (p[0] == data['identificacion']):
            return jsonify({'estado': 'error', 
                            'mensaje': 'Identificación Duplicada'})
    #crea un nueva persona en forma de lista
    nueva_persona = [
        data['identificacion'],
        data['nombres'],
        data['fecha'],
        data['genero'],
        data['ciudad'],
        data['movil'],
        data['mail'],
        float(data['salario'])  #aseguramos que sea de tipo float
    ]

    personas.append(nueva_persona) #agrega la nueva persona a la lista
    guardar_datos(personas)     #guarda los cambios en el archivo fisico

    return jsonify({'estado': 'ok'})

#LISTAR
# Ruta para obtener todas las personas (GET)
@app.route('/personas', methods=['GET'])
def listar():
    return jsonify(cargar_datos())  # Devuelve la lista de personas en formato JSON

#ACTUALIZAAR

# Ruta para editar una persona (PUT)
@app.route('/persona/<identificacion>', methods=['PUT'])
def editar(identificacion):
    #recibiendo datos en formato JSON desde el cliente
    data = request.json
    personas = cargar_datos()

    for i, p in enumerate(personas):
        if p[0] == identificacion:  # Busca la persona a editar
            # Reemplaza todos los campos por los nuevos valores
            personas[i] = [
                identificacion,
                data['nombres'],
                data['fecha'],
                data['genero'],
                data['ciudad'],
                data['movil'],
                data['mail'],
                float(data['salario'])
            ]
            guardar_datos(personas)
            # respuesta en formato JSON que envía el servidor Flask al navegador o cliente
            return jsonify({'estado': 'ok'})

    return jsonify({'estado': 'error', 'mensaje': 'No encontrado'})

#ELIMINAR
# Ruta para eliminar una persona por su identificación (DELETE)
@app.route('/persona/<identificacion>', methods=['DELETE'])
def eliminar(identificacion):
    personas = cargar_datos()
    # Elimina la persona cuyo ID coincida
    personas = [p for p in personas if p[0] != identificacion]
    guardar_datos(personas)
    return jsonify({'estado': 'ok'})


if __name__ == '__main__':
    app.run(debug=True)