
edad=0
#edad = int(input("EDAD: "))
try:
    edad = int(input("EDAD: "))
except ValueError:
    print("EDAD NO VALIDA")

print( edad )