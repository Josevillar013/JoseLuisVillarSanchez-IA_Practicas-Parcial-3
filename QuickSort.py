def quicksort(arr):
    # Si la lista tiene 1 o 0 elementos, ya está ordenada
    if len(arr) <= 1:
        return arr
    # Selecciona el pivote como el elemento del medio
    pivot = arr[len(arr) // 2]
    # Crea una lista con los elementos menores que el pivote
    left = [x for x in arr if x < pivot]
    # Crea una lista con los elementos iguales al pivote
    middle = [x for x in arr if x == pivot]
    # Crea una lista con los elementos mayores que el pivote
    right = [x for x in arr if x > pivot]
    # Llama recursivamente a quicksort y concatena los resultados
    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
if __name__ == "__main__":
    lista = [3, 6, 8, 10, 1, 2, 1]
    print("Lista original:", lista)
    print("Lista ordenada:", quicksort(lista))