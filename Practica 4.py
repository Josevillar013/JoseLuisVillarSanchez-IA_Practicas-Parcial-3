import sys  # Importa el módulo sys para acceder a sys.maxsize

def prim_mst(graph):
    num_vertices = len(graph)  # Obtiene el número de vértices del grafo
    selected = [False] * num_vertices  # Lista para marcar los vértices seleccionados
    selected[0] = True  # Selecciona el primer vértice como punto de inicio
    mst_edges = []  # Lista para almacenar las aristas del árbol de expansión mínima

    print("Paso a paso del algoritmo de Prim:\n")
    for _ in range(num_vertices - 1):  # Repite hasta que se seleccionen todos los vértices menos uno
        min_weight = sys.maxsize  # Inicializa el peso mínimo con el valor máximo posible
        x = y = 0  # Variables para almacenar los índices de los vértices de la arista mínima
        for i in range(num_vertices):  # Recorre todos los vértices
            if selected[i]:  # Si el vértice está seleccionado
                for j in range(num_vertices):  # Recorre todos los vértices adyacentes
                    if (not selected[j]) and graph[i][j]:  # Si el vértice no está seleccionado y hay arista
                        if min_weight > graph[i][j]:  # Si el peso es menor que el mínimo actual
                            min_weight = graph[i][j]  # Actualiza el peso mínimo
                            x, y = i, j  # Guarda los índices de los vértices de la arista mínima
        selected[y] = True  # Marca el vértice y como seleccionado
        mst_edges.append((x, y, graph[x][y]))  # Añade la arista seleccionada al árbol
        print(f"Seleccionada arista ({x} - {y}) con peso {graph[x][y]}")  # Muestra la arista seleccionada
        print(f"Vertices seleccionados: {[i for i, sel in enumerate(selected) if sel]}\n")  # Muestra los vértices seleccionados
    return mst_edges  # Devuelve la lista de aristas del árbol de expansión mínima

def main():
    # Ejemplo de grafo: matriz de adyacencia
    graph = [
        [0, 2, 0, 6, 0],   # Fila 0: conexiones del vértice 0
        [2, 0, 3, 8, 5],   # Fila 1: conexiones del vértice 1
        [0, 3, 0, 0, 7],   # Fila 2: conexiones del vértice 2
        [6, 8, 0, 0, 9],   # Fila 3: conexiones del vértice 3
        [0, 5, 7, 9, 0]    # Fila 4: conexiones del vértice 4
    ]
    print("Grafo de entrada (matriz de adyacencia):")
    for row in graph:  # Imprime cada fila de la matriz de adyacencia
        print(row)
    print("\nIniciando algoritmo de Prim...\n")
    mst = prim_mst(graph)  # Llama a la función para calcular el árbol de expansión mínima
    print("Árbol de expansión mínima resultante:")
    for edge in mst:  # Imprime cada arista del árbol de expansión mínima
        print(f"{edge[0]} - {edge[1]} (peso {edge[2]})")

if __name__ == "__main__":  # Comprueba si el script se está ejecutando directamente
    main()  # Llama a la función principal la cual inicia el programaml
    