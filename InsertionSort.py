def insertion_sort(arr):  # Define la función insertion_sort que recibe una lista 'arr'
    for i in range(1, len(arr)):  # Recorre la lista desde el segundo elemento hasta el final
        key = arr[i]  # Guarda el valor actual en 'key'
        j = i - 1  # Inicializa 'j' como el índice anterior a 'i'
        while j >= 0 and arr[j] > key:  # Mientras 'j' sea válido y el elemento en 'arr[j]' sea mayor que 'key'
            arr[j + 1] = arr[j]  # Desplaza el elemento hacia la derecha
            j -= 1  # Decrementa 'j' para comparar con el elemento anterior
        arr[j + 1] = key  # Inserta 'key' en la posición correcta
    return arr  # Devuelve la lista ordenada

# Ejemplo de uso
if __name__ == "__main__":  # Comprueba si el archivo se está ejecutando directamente
    lista = [12, 11, 13, 5, 6]  # Define una lista de ejemplo
    print("Lista original:", lista)  # Imprime la lista original
    insertion_sort(lista)  # Llama a la función para ordenar la lista
    print("Lista ordenada:", lista)  # Imprime la lista ya ordenada