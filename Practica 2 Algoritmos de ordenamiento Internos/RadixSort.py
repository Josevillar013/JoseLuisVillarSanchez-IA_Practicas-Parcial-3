def counting_sort(arr, exp):
    n = len(arr)  # Obtener el tamaño del arreglo
    output = [0] * n  # Inicializar el arreglo de salida con ceros
    count = [0] * 10  # Inicializar el arreglo de conteo para los dígitos (0-9)

    # Contar ocurrencias de cada dígito en la posición actual (exp)
    for i in range(n):
        index = (arr[i] // exp) % 10  # Obtener el dígito relevante
        count[index] += 1  # Incrementar el conteo para ese dígito

    # Modificar count[i] para que contenga la posición real de este dígito en output
    for i in range(1, 10):
        count[i] += count[i - 1]  # Sumar el conteo anterior

    # Construir el arreglo de salida usando count para ubicar los elementos
    i = n - 1  # Empezar desde el final del arreglo original
    while i >= 0:
        index = (arr[i] // exp) % 10  # Obtener el dígito relevante
        output[count[index] - 1] = arr[i]  # Colocar el elemento en la posición correcta
        count[index] -= 1  # Disminuir el conteo para ese dígito
        i -= 1  # Pasar al elemento anterior

    # Copiar el arreglo de salida al arreglo original para la siguiente iteración
    for i in range(n):
        arr[i] = output[i]  # Copiar cada elemento

def radix_sort(arr):
    if not arr:  # Verifica si el arreglo está vacío
        return arr  # Si está vacío, retorna el mismo arreglo
    max_num = max(arr)  # Encuentra el valor máximo en el arreglo
    exp = 1  # Inicializa el exponente para acceder a cada dígito (unidades, decenas, etc.)
    while max_num // exp > 0:  # Itera mientras haya dígitos que procesar
        counting_sort(arr, exp)  # Ordena el arreglo según el dígito actual
        exp *= 10  # Pasa al siguiente dígito más significativo

# Ejemplo de uso
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Arreglo original:", arr)
    radix_sort(arr)
    print("Arreglo ordenado:", arr)