def suma(num1,num2):
    return num1 + num2

def resta(num1,num2):
    return num1 - num2

def multiplicacion(num1,num2):
    return num1 * num2

def division(num1,num2):
    return num1 / num2

def divisionEntera(num1,num2):
    return num1 // num2

num1 = float(input("Introduce un número: "))
num2 = float(input("Introduce un segundo número: "))

print("La suma de los numeros", suma(num1,num2))
print("La resta de los numeros", resta(num1,num2))
print("La multiplicación de los numeros", multiplicacion(num1,num2))
print("La división entera de los numeros", divisionEntera(num1,num2))
print("La división de los numeros", division(num1,num2))