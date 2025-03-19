#son listas inmutables, NO se pueden insertar nuevos elementos, NO actualizar, NO eliminar
#si desea aplicar operaciones pase la tula a un lista con  list(tupla)

constantes = (1400000, 200000, 0.4)  #se trabaja con indices
tupla = ("programacion", "ingles", "proyectos", "habilidades")

#constantes[0] = 1600000   #NO se puede modificar es INMUTABLE
#del constantes[0]

print(f"CANTIDAD VECES DE INGLES: ", tupla.count("ingles"))
print(f"CANTIDAD ELEMENTOS: ", len(tupla))

