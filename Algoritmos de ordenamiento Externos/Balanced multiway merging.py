import heapq  # Importa el módulo heapq para usar una cola de prioridad (heap)

def balanced_multiway_merge(input_files, output_file):
    """
    Realiza un merge balanceado de múltiples archivos ordenados.
    Cada archivo de entrada debe estar ordenado.
    El resultado se escribe en output_file, también ordenado.
    """
    open_files = [open(f, 'r') for f in input_files]  # Abre todos los archivos de entrada en modo lectura
    heap = []  # Inicializa una lista vacía que funcionará como heap

    # Inicializa el heap con el primer elemento de cada archivo
    for idx, f in enumerate(open_files):  # Itera sobre los archivos abiertos y sus índices
        line = f.readline()  # Lee la primera línea del archivo actual
        if line:  # Si la línea no está vacía
            heapq.heappush(heap, (int(line.strip()), idx))  # Inserta una tupla (valor, índice de archivo) en el heap

    with open(output_file, 'w') as out:  # Abre el archivo de salida en modo escritura
        while heap:  # Mientras el heap no esté vacío
            value, idx = heapq.heappop(heap)  # Extrae el menor elemento del heap (valor, índice de archivo)
            out.write(f"{value}\n")  # Escribe el valor en el archivo de salida
            next_line = open_files[idx].readline()  # Lee la siguiente línea del archivo correspondiente
            if next_line:  # Si la línea no está vacía
                heapq.heappush(heap, (int(next_line.strip()), idx))  # Inserta el nuevo valor en el heap

    for f in open_files:  # Itera sobre todos los archivos abiertos
        f.close()  # Cierra cada archivo

if __name__ == "__main__":
    # Ejemplo de uso:
    # Supón que tienes archivos 'sorted1.txt', 'sorted2.txt', 'sorted3.txt'
    input_files = ['sorted1.txt', 'sorted2.txt', 'sorted3.txt']  # Lista de archivos de entrada ordenados
    output_file = 'merged_output.txt'  # Nombre del archivo de salida
    balanced_multiway_merge(input_files, output_file)  # Llama a la función de merge
    print(f"Archivos {input_files} fusionados en {output_file}")  # Imprime mensaje de éxito