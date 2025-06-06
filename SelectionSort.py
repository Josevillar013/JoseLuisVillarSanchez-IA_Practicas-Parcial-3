def selection_sort(arr):
    n = len(arr)  # Obtiene la longitud de la lista
    for i in range(n):  # Recorre cada elemento de la lista
        min_idx = i  # Supone que el elemento actual es el mínimo
        for j in range(i+1, n):  # Busca el elemento más pequeño en el resto de la lista
            if arr[j] < arr[min_idx]:  # Si encuentra un elemento menor
                min_idx = j  # Actualiza el índice del mínimo
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambia el elemento actual con el mínimo encontrado

if __name__ == "__main__":
    datos = [64, 25, 12, 22, 11]  # Lista de ejemplo a ordenar
    print("Lista original:", datos)  # Muestra la lista original
    selection_sort(datos)  # Llama a la función de ordenamiento
    print("Lista ordenada:", datos)  # Muestra la lista ordenada