# Intercambio de valores entre dos variables en Python

def intercambio(a, b):
    print(f"Antes del intercambio: a = {a}, b = {b}")
    # Intercambio usando una variable temporal
    temp = a
    a = b
    b = temp
    print(f"Después del intercambio: a = {a}, b = {b}")
    return a, b

if __name__ == "__main__":
    x = int(input("Introduce el valor de x: "))
    y = int(input("Introduce el valor de y: "))
    intercambio(x, y)