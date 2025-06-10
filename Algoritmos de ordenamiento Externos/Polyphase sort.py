import heapq  # Importa el módulo heapq para trabajar con colas de prioridad (heaps)
import os  # Importa el módulo os para operaciones del sistema de archivos

def split_into_runs(input_file, run_size):
    runs = []  # Lista para almacenar los nombres de los archivos de runs temporales
    with open(input_file, 'r') as f:  # Abre el archivo de entrada en modo lectura
        while True:  # Bucle infinito hasta que no haya más líneas
            lines = []  # Lista para almacenar los números de la run actual
            for _ in range(run_size):  # Lee hasta run_size líneas
                line = f.readline()  # Lee una línea del archivo
                if not line:  # Si no hay más líneas, termina el bucle
                    break
                lines.append(int(line.strip()))  # Convierte la línea a entero y la agrega a la lista
            if not lines:  # Si no se leyeron líneas, termina el bucle principal
                break
            lines.sort()  # Ordena los números leídos
            run_file = f'run_{len(runs)}.txt'  # Nombre del archivo temporal para la run
            with open(run_file, 'w') as rf:  # Abre el archivo temporal en modo escritura
                for num in lines:  # Escribe cada número ordenado en el archivo
                    rf.write(f"{num}\n")
            runs.append(run_file)  # Agrega el nombre del archivo de la run a la lista
    return runs  # Devuelve la lista de archivos de runs generados

def merge_runs(run_files, output_file):
    files = [open(run, 'r') for run in run_files]  # Abre todos los archivos de runs en modo lectura
    heap = []  # Inicializa una lista para usar como heap (cola de prioridad)
    for i, f in enumerate(files):  # Itera sobre los archivos abiertos
        line = f.readline()  # Lee la primera línea de cada archivo
        if line:  # Si la línea no está vacía
            heapq.heappush(heap, (int(line.strip()), i))  # Inserta el valor y el índice del archivo en el heap
    with open(output_file, 'w') as out:  # Abre el archivo de salida en modo escritura
        while heap:  # Mientras el heap no esté vacío
            val, idx = heapq.heappop(heap)  # Extrae el valor más pequeño y el índice del archivo correspondiente
            out.write(f"{val}\n")  # Escribe el valor en el archivo de salida
            line = files[idx].readline()  # Lee la siguiente línea del archivo correspondiente
            if line:  # Si la línea no está vacía
                heapq.heappush(heap, (int(line.strip()), idx))  # Inserta el nuevo valor en el heap
    for f in files:  # Itera sobre los archivos abiertos
        f.close()  # Cierra cada archivo
    for run in run_files:  # Itera sobre los nombres de los archivos de runs
        os.remove(run)  # Elimina cada archivo temporal de run

def polyphase_sort(input_file, output_file, run_size=100):
    runs = split_into_runs(input_file, run_size)  # Divide el archivo de entrada en runs ordenados
    while len(runs) > 1:  # Mientras haya más de un run, sigue fusionando
        new_runs = []  # Lista para almacenar los nuevos runs fusionados
        for i in range(0, len(runs), 2):  # Itera sobre los runs de dos en dos
            if i+1 < len(runs):  # Si hay un par de runs para fusionar
                merged_run = f"merged_{i//2}.txt"  # Nombre del archivo para el run fusionado
                merge_runs([runs[i], runs[i+1]], merged_run)  # Fusiona los dos runs en uno solo
                new_runs.append(merged_run)  # Agrega el run fusionado a la lista de nuevos runs
            else:
                new_runs.append(runs[i])  # Si hay un run sin pareja, lo pasa tal cual a la siguiente ronda
        runs = new_runs  # Actualiza la lista de runs con los nuevos runs fusionados
    os.rename(runs[0], output_file)  # Renombra el último run restante como archivo de salida final

# Ejemplo de uso:
# polyphase_sort('input.txt', 'sorted.txt', run_size=100)