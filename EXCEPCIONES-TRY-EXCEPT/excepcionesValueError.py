
edad=0
try:
    edad = int(input("EDAD: "))
except ValueError:
    print("EDAD NO VALIDA")

print( edad )