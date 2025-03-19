#es una estructura, hace referencia a que cada elmento esta compuesto por CLAVE:VALOR

departamentos = {
    'caldas'   :'Manizales',
    'antioquia':'Medellín',
    'tolima'   :'Ibague',
    }
departamentos['caldas'] = 'MANIZALES'  #SI la clave ya existe, sobreescribe el nuevo valor
departamentos['valle'] = 'Cali'        #si la clave no esta crea una nueva clave valor
del departamentos['tolima']            #si la clave existe se elimina la clave valor

print(f"DEPARTAMENTOS y CAPITALES: ", departamentos)
print(f"TUPLAS DE CLAVE VALOR: ", departamentos.items())
print(f"DEPARTAMENTOS: ", departamentos.keys())
print(f"CAPITALES: ", departamentos.values())
print('*****')
for clave_valor in departamentos.items():
    print(clave_valor)
#eliminar

generos = {
    'm': 'Másculino',
    'f': 'Femenino',
    'o': 'Otro'
}

for clave in generos.keys():
    if (clave == 'm'):
        print('existe')