import sys  # Importa el módulo sys (aunque no se usa en este código)

def dijkstra(graph, start):
    visited = set()  # Conjunto para almacenar los nodos visitados
    distance = {node: float('inf') for node in graph}  # Diccionario de distancias mínimas desde el nodo inicial
    previous = {node: None for node in graph}  # Diccionario para reconstruir el camino más corto
    distance[start] = 0  # La distancia al nodo inicial es 0

    print(f"Estado inicial: {distance}")  # Muestra el estado inicial de las distancias

    while visited != set(graph):  # Mientras queden nodos por visitar
        # Encuentra el nodo no visitado con la menor distancia
        current = min(
            (node for node in graph if node not in visited),
            key=lambda node: distance[node]
        )
        print(f"\nVisitando nodo: {current} (distancia actual: {distance[current]})")  # Muestra el nodo actual

        for neighbor, weight in graph[current].items():  # Itera sobre los vecinos del nodo actual
            if neighbor not in visited:  # Si el vecino no ha sido visitado
                new_dist = distance[current] + weight  # Calcula la nueva distancia
                if new_dist < distance[neighbor]:  # Si la nueva distancia es menor que la actual
                    print(f"Actualizando distancia de {neighbor}: {distance[neighbor]} -> {new_dist}")  # Muestra la actualización
                    distance[neighbor] = new_dist  # Actualiza la distancia
                    previous[neighbor] = current  # Actualiza el nodo previo

        visited.add(current)  # Marca el nodo actual como visitado
        print(f"Distancias actuales: {distance}")  # Muestra las distancias actuales
        print(f"Nodos visitados: {visited}")  # Muestra los nodos visitados

    print("\nResultado final:")  # Muestra el resultado final
    for node in graph:  # Para cada nodo en el grafo
        path = []  # Lista para almacenar el camino más corto
        curr = node  # Nodo actual para reconstruir el camino
        while curr is not None:  # Mientras haya un nodo previo
            path.insert(0, curr)  # Inserta el nodo al inicio del camino
            curr = previous[curr]  # Avanza al nodo previo
        print(f"Camino más corto a {node}: {' -> '.join(path)} (distancia: {distance[node]})")  # Muestra el camino y la distancia

# Ejemplo de uso
if __name__ == "__main__":
    # Grafo de ejemplo (puedes modificarlo)
    graph = {
        'A': {'B': 1, 'C': 4},  # Nodo A conectado a B (1) y C (4)
        'B': {'A': 1, 'C': 2, 'D': 5},  # Nodo B conectado a A (1), C (2), D (5)
        'C': {'A': 4, 'B': 2, 'D': 1},  # Nodo C conectado a A (4), B (2), D (1)
        'D': {'B': 5, 'C': 1}  # Nodo D conectado a B (5) y C (1)
    }
    start_node = 'A'  # Nodo inicial
    dijkstra(graph, start_node)  # Llama a la función dijkstra con el grafo y el nodo inicial