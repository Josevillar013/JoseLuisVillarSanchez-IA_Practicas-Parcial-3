import os  # Importa el módulo os para operaciones del sistema operativo

def distribute_initial_runs(input_file, output_files, run_size):
    """
    Distributes initial runs from the input file into multiple output files.
    Each run is a sorted sequence of 'run_size' elements.
    """
    # Abre los archivos de salida para escritura
    outs = [open(f, 'w') for f in output_files]
    out_index = 0  # Índice para alternar entre archivos de salida

    with open(input_file, 'r') as infile:  # Abre el archivo de entrada para lectura
        while True:  # Bucle principal para procesar todo el archivo
            lines = []  # Lista para almacenar los elementos de la corrida actual
            for _ in range(run_size):  # Lee hasta 'run_size' líneas
                line = infile.readline()  # Lee una línea del archivo
                if not line:  # Si no hay más líneas, termina el bucle interno
                    break
                lines.append(int(line.strip()))  # Convierte la línea a entero y la agrega a la lista
            if not lines:  # Si no se leyeron líneas, termina el bucle principal
                break
            lines.sort()  # Ordena la corrida actual
            for num in lines:  # Escribe cada número ordenado en el archivo de salida correspondiente
                outs[out_index].write(f"{num}\n")
            out_index = (out_index + 1) % len(outs)  # Cambia al siguiente archivo de salida

    for f in outs:  # Cierra todos los archivos de salida
        f.close()

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "input.txt"  # Nombre del archivo de entrada
    with open(input_file, 'w') as f:  # Crea el archivo de entrada con datos de ejemplo
        for num in [8, 3, 7, 1, 9, 2, 6, 5, 4, 0]:
            f.write(f"{num}\n")

    output_files = ["run1.txt", "run2.txt"]  # Nombres de los archivos de salida
    run_size = 3  # Tamaño de cada corrida

    distribute_initial_runs(input_file, output_files, run_size)  # Llama a la función para distribuir las corridas

    for fname in output_files:  # Imprime el contenido de cada archivo de salida
        print(f"Contents of {fname}:")
        with open(fname, 'r') as f:
            print(f.read())
