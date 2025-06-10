def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contar ocurrencias de dígitos
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Cambiar count[i] para que contenga la posición real
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo de salida
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiar al arreglo original
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Ejemplo de uso
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Arreglo original:", arr)
    radix_sort(arr)
    print("Arreglo ordenado:", arr)