def straight_merge_sort(arr):  # Define la función de ordenamiento Straight Merge Sort
    width = 1                  # Inicializa el tamaño del subarreglo a fusionar
    n = len(arr)               # Obtiene la longitud del arreglo
    result = arr[:]            # Crea una copia del arreglo original
    while width < n:           # Mientras el tamaño del subarreglo sea menor que el arreglo
        for i in range(0, n, 2 * width):  # Itera sobre el arreglo en pasos de 2*width
            left = i                       # Índice inicial del primer subarreglo
            mid = min(i + width, n)        # Índice final del primer subarreglo/inicio del segundo
            right = min(i + 2 * width, n)  # Índice final del segundo subarreglo
            merged = []                    # Lista temporal para almacenar la fusión
            l, r = left, mid               # Inicializa los punteros para ambos subarreglos
            while l < mid and r < right:   # Mientras haya elementos en ambos subarreglos
                if result[l] <= result[r]: # Compara los elementos actuales de ambos subarreglos
                    merged.append(result[l]) # Agrega el menor a la lista fusionada
                    l += 1                   # Avanza el puntero del primer subarreglo
                else:
                    merged.append(result[r]) # Agrega el menor a la lista fusionada
                    r += 1                   # Avanza el puntero del segundo subarreglo
            merged.extend(result[l:mid])     # Agrega los elementos restantes del primer subarreglo
            merged.extend(result[r:right])   # Agrega los elementos restantes del segundo subarreglo
            result[left:right] = merged      # Reemplaza la sección correspondiente en el arreglo original
        width *= 2                          # Duplica el tamaño del subarreglo para la siguiente iteración
    return result                           # Devuelve el arreglo ordenado

if __name__ == "__main__":                  # Punto de entrada principal del programa
    arr = [38, 27, 43, 3, 9, 82, 10]        # Define el arreglo a ordenar
    print("Original array:", arr)           # Imprime el arreglo original
    sorted_arr = straight_merge_sort(arr)   # Llama a la función de ordenamiento
    print("Sorted array:", sorted_arr)      # Imprime el arreglo ordenado