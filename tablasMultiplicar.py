"""for i in range(1,10+1):
    print(f"Tabla de multiplicar del {i}")
    for j in range(1,10+1):
        print(f"{i} x {j} = {i*j}")
"""
def tablas(a):
    for i in range(1,11):
        print(f"{a} x {i} = {a*i}")

for i in range(1,11):
    print(tablas(i))
