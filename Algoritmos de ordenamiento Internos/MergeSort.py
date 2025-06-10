def merge_sort(arr):  # Define la función merge_sort que toma una lista arr como argumento
    if len(arr) > 1:  # Si la longitud de arr es mayor que 1, continúa (caso base de la recursión)
        mid = len(arr) // 2  # Calcula el punto medio de la lista
        left_half = arr[:mid]  # Divide la lista en la mitad izquierda
        right_half = arr[mid:]  # Divide la lista en la mitad derecha

        merge_sort(left_half)  # Llama recursivamente a merge_sort en la mitad izquierda
        merge_sort(right_half)  # Llama recursivamente a merge_sort en la mitad derecha

        i = j = k = 0  # Inicializa los índices para recorrer left_half, right_half y arr

        # Mezcla las dos mitades ordenadas
        while i < len(left_half) and j < len(right_half):  # Mientras haya elementos en ambas mitades
            if left_half[i] < right_half[j]:  # Si el elemento actual de left_half es menor
                arr[k] = left_half[i]  # Coloca ese elemento en la posición k de arr
                i += 1  # Avanza el índice de left_half
            else:
                arr[k] = right_half[j]  # Coloca el elemento de right_half en arr
                j += 1  # Avanza el índice de right_half
            k += 1  # Avanza el índice de arr

        # Copia los elementos restantes de left_half, si hay
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copia los elementos restantes de right_half, si hay
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    merge_sort(arr)
    print("Sorted array:", arr)