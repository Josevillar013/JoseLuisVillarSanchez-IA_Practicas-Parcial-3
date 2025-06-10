def bubble_sort(arr):
    # Obtiene la longitud de la lista
    n = len(arr)
    # Recorre toda la lista
    for i in range(n):
        # Recorre la lista desde el principio hasta el elemento no ordenado
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente, los intercambia
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambio de elementos
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

if __name__ == "__main__":
    datos = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", datos)

    # Bubble Sort
    bubble_sorted = datos.copy()
    bubble_sort(bubble_sorted)
    print("Ordenado con Bubble Sort:", bubble_sorted)

    # Selection Sort
    selection_sorted = datos.copy()
    selection_sort(selection_sorted)
    print("Ordenado con Selection Sort:", selection_sorted)
    