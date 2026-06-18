print("Calculadora con menu")

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))

print("1.- Sumar")
print("2.- Restar")
opcion = input("Seleccione una opcion: ")

if opcion == "1":
    print("La suma es:", num1 + num2)
elif opcion == "2":
    print("La resta es:", num1 - num2)
else:
    print("Opcion no valida")
