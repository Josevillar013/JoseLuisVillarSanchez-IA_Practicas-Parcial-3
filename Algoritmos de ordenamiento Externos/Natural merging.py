def natural_merge_sort(arr):  # Define la función principal de ordenamiento natural por mezcla
    def find_runs(arr):  # Función interna para encontrar secuencias ordenadas (runs)
        runs = []  # Lista para almacenar las secuencias encontradas
        n = len(arr)  # Longitud del arreglo
        i = 0  # Índice inicial
        while i < n:  # Mientras no se llegue al final del arreglo
            run = [arr[i]]  # Comienza una nueva secuencia con el elemento actual
            i += 1  # Avanza al siguiente elemento
            while i < n and arr[i-1] <= arr[i]:  # Mientras la secuencia siga ordenada
                run.append(arr[i])  # Agrega el elemento a la secuencia
                i += 1  # Avanza al siguiente elemento
            runs.append(run)  # Agrega la secuencia encontrada a la lista de secuencias
        return runs  # Devuelve todas las secuencias encontradas

    def merge(left, right):  # Función interna para mezclar dos secuencias ordenadas
        result = []  # Lista para almacenar el resultado de la mezcla
        i = j = 0  # Índices para recorrer las dos secuencias
        while i < len(left) and j < len(right):  # Mientras haya elementos en ambas secuencias
            if left[i] <= right[j]:  # Si el elemento de la izquierda es menor o igual
                result.append(left[i])  # Agrega el elemento de la izquierda
                i += 1  # Avanza en la secuencia izquierda
            else:
                result.append(right[j])  # Agrega el elemento de la derecha
                j += 1  # Avanza en la secuencia derecha
        result.extend(left[i:])  # Agrega los elementos restantes de la izquierda (si hay)
        result.extend(right[j:])  # Agrega los elementos restantes de la derecha (si hay)
        return result  # Devuelve la secuencia mezclada

    if len(arr) <= 1:  # Si el arreglo tiene 1 o 0 elementos, ya está ordenado
        return arr  # Devuelve el arreglo tal cual

    while True:  # Bucle principal del algoritmo
        runs = find_runs(arr)  # Encuentra todas las secuencias ordenadas en el arreglo
        if len(runs) == 1:  # Si solo hay una secuencia, el arreglo está ordenado
            break  # Sale del bucle
        new_arr = []  # Lista para almacenar el nuevo arreglo tras mezclar
        i = 0  # Índice para recorrer las secuencias
        while i < len(runs):  # Mientras haya secuencias por mezclar
            if i + 1 < len(runs):  # Si hay al menos dos secuencias para mezclar
                merged = merge(runs[i], runs[i+1])  # Mezcla dos secuencias consecutivas
                new_arr.extend(merged)  # Agrega la secuencia mezclada al nuevo arreglo
                i += 2  # Avanza dos posiciones
            else:
                new_arr.extend(runs[i])  # Si queda una sola secuencia, la agrega tal cual
                i += 1  # Avanza una posición
        arr = new_arr  # Actualiza el arreglo con el resultado de la mezcla
    return arr  # Devuelve el arreglo ordenado

# Ejemplo de uso
if __name__ == "__main__":  # Si el archivo se ejecuta directamente
    datos = [5, 1, 4, 2, 8, 3, 7, 6]  # Lista de ejemplo a ordenar
    print("Original:", datos)  # Muestra la lista original
    ordenado = natural_merge_sort(datos)  # Ordena la lista usando el algoritmo
    print("Ordenado:", ordenado)  # Muestra la lista ordenada