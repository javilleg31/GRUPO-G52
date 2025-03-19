#un conjunto es una estructura con elementos, agrupados entre llaves
#add - discard - union - inteseccion - diferencia
impares = {}
pares = {}

impares = {1, 3, 5, 7, 1, 3, 5}
pares   = {2, 4, 6, 8, 7}

print(f"IMPARES: ", impares)
print(f"PARES  : ", pares)

impares.add("9")
print(f"IMPARES: ", impares)

impares.discard("9")
print(f"IMPARES: ", impares)

union = impares.union(pares)                # 1,2,3,4,5,6,7,8,
interseccion = impares.intersection(pares)  # vacio
diferencia = impares.difference(pares)      # 1,3,5,7,9

print(f"UNION: ", union)
print(f"INTERSECCION: ", interseccion)
print(f"DIFERENCIA: ", diferencia)

print(f"MAXIMO: ", max(union))
print(f"MINIMO: ", min(union))

