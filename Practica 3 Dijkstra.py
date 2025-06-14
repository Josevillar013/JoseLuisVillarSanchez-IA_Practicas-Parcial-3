import heapq # Importa el módulo heapq para usar una cola de prioridad (min-heap).

def dijkstra_simulation(graph, start_node):
    """
    Simula el algoritmo de Dijkstra paso a paso y lo imprime en la consola.

    Args:
        graph (dict): Un diccionario que representa el grafo.
                      Las claves son los nodos y los valores son diccionarios
                      de nodos vecinos y sus pesos.
                      Ej: {'A': {'B': 4, 'C': 2}}
        start_node (str): El nodo desde el cual iniciar la búsqueda.
    """
    print("--- SIMULADOR DEL ALGORITMO DE DIJKSTRA ---") # Imprime un encabezado para el simulador.
    print(f"\nGrafo de entrada:") # Imprime el encabezado para el grafo de entrada.
    for node, edges in graph.items(): # Itera sobre cada nodo y sus conexiones en el grafo.
        print(f"  {node}: {edges}") # Imprime el nodo y sus aristas salientes con sus pesos.

    print(f"\nNodo de inicio: {start_node}\n") # Imprime el nodo desde el cual comenzará la simulación.

    # Inicialización
    # Distancias: Un diccionario para almacenar las distancias más cortas conocidas desde el nodo de inicio.
    # Inicialmente, todas son infinitas, excepto el nodo de inicio que es 0.
    distances = {node: float('infinity') for node in graph} # Inicializa las distancias de todos los nodos a infinito.
    distances[start_node] = 0 # La distancia del nodo de inicio a sí mismo es 0.

    # Pq: Cola de prioridad para almacenar (distancia, nodo).
    # Usaremos heapq para implementar una min-heap.
    pq = [(0, start_node)] # Inicializa la cola de prioridad con el nodo de inicio y su distancia 0.

    # Visited: Conjunto para mantener un registro de los nodos visitados.
    # Los nodos visitados son aquellos para los que ya hemos encontrado la distancia más corta definitiva.
    visited = set() # Inicializa un conjunto vacío para los nodos visitados.

    # Previous nodes: Diccionario para reconstruir el camino más corto.
    # Almacena el nodo anterior en el camino más corto conocido hasta el momento.
    previous_nodes = {node: None for node in graph} # Inicializa los nodos previos a None para todos los nodos.

    step = 0 # Inicializa el contador de pasos de la simulación.
    print("--- PASO A PASO ---") # Imprime un encabezado para la sección paso a paso.

    while pq: # El bucle continúa mientras la cola de prioridad no esté vacía.
        step += 1 # Incrementa el contador de pasos.
        print(f"\n--- Paso {step} ---") # Imprime el número del paso actual.
        print(f"Distancias actuales: {distances}") # Muestra las distancias actuales conocidas a todos los nodos.
        print(f"Nodos visitados: {visited}") # Muestra los nodos que ya han sido visitados.

        # Extraer el nodo con la distancia más pequeña de la cola de prioridad
        # heapq.heappop siempre devuelve el elemento más pequeño del heap.
        current_distance, current_node = heapq.heappop(pq) # Extrae el nodo con la menor distancia de la cola de prioridad.
        print(f"Procesando nodo: '{current_node}' con distancia '{current_distance}'") # Informa qué nodo se está procesando.

        # Si ya visitamos este nodo, continuar (ya encontramos el camino más corto a él)
        # Esto es importante porque un nodo puede ser añadido a la cola de prioridad varias veces
        # con diferentes distancias si se encuentran caminos más cortos.
        if current_node in visited: # Comprueba si el nodo actual ya ha sido visitado.
            print(f"  El nodo '{current_node}' ya ha sido visitado. Saltando.") # Si ya fue visitado, lo indica y salta.
            continue # Pasa a la siguiente iteración del bucle.

        # Marcar el nodo como visitado
        # Una vez visitado, su distancia actual es la distancia más corta definitiva.
        visited.add(current_node) # Añade el nodo actual al conjunto de nodos visitados.
        print(f"  Marcado '{current_node}' como visitado.") # Informa que el nodo ha sido marcado como visitado.

        # Recorrer los nodos vecinos
        print(f"  Explorando vecinos de '{current_node}':") # Imprime un encabezado para explorar vecinos.
        # Itera sobre los nodos conectados al current_node y los pesos de esas conexiones.
        for neighbor, weight in graph[current_node].items(): # Itera sobre los vecinos del nodo actual y el peso de la arista.
            print(f"    Considerando vecino '{neighbor}' con peso {weight}.") # Informa qué vecino se está considerando.
            # Calcula la distancia a este vecino a través del current_node.
            distance = current_distance + weight # Calcula la distancia total para llegar al vecino a través del nodo actual.

            # Si se encuentra un camino más corto al vecino
            # Compara la nueva distancia calculada con la distancia actual conocida al vecino.
            if distance < distances[neighbor]: # Comprueba si la nueva distancia es menor que la distancia conocida del vecino.
                distances[neighbor] = distance # Si es menor, actualiza la distancia del vecino.
                previous_nodes[neighbor] = current_node # Actualiza el nodo previo del vecino al nodo actual.
                heapq.heappush(pq, (distance, neighbor)) # Añade el vecino (con su nueva distancia) a la cola de prioridad.
                print(f"      Distancia a '{neighbor}' actualizada a {distance}. Añadido a la cola de prioridad.") # Informa la actualización.
            else:
                print(f"      La distancia {distance} no es más corta que la distancia actual a '{neighbor}' ({distances[neighbor]}).") # Informa que no se encontró un camino más corto.

    print("\n--- SIMULACIÓN FINALIZADA ---") # Imprime un mensaje indicando el final de la simulación.
    print("\nRESULTADOS FINALES:") # Imprime un encabezado para los resultados finales.
    print("Distancias más cortas desde el nodo de inicio:") # Imprime un encabezado para las distancias.
    for node, distance in distances.items(): # Itera sobre todos los nodos y sus distancias finales.
        if distance == float('infinity'): # Comprueba si un nodo es inalcanzable.
            print(f"  A {node}: No se pudo alcanzar") # Indica que el nodo no fue alcanzable.
        else:
            print(f"  A {node}: {distance}") # Muestra la distancia más corta al nodo.

    print("\nCaminos más cortos (reconstruidos):") # Imprime un encabezado para los caminos reconstruidos.
    for target_node in graph: # Itera sobre cada nodo en el grafo para reconstruir su camino.
        if distances[target_node] == float('infinity'): # Si el nodo es inalcanzable, lo indica.
            print(f"  A {target_node}: No accesible") # Mensaje para nodo inalcanzable.
            continue # Salta al siguiente nodo.
        path = [] # Inicializa una lista para almacenar el camino.
        current = target_node # Empieza desde el nodo objetivo.
        # Reconstruye el camino yendo hacia atrás desde el nodo objetivo usando previous_nodes.
        while current is not None: # Continúa mientras haya un nodo previo.
            path.insert(0, current) # Inserta el nodo actual al principio de la lista para construir el camino en orden inverso.
            current = previous_nodes[current] # Mueve al nodo previo.
        print(f"  A {target_node}: {' -> '.join(path)}") # Imprime el camino reconstruido al nodo objetivo.


# --- GRAFO DE EJEMPLO ---
# Puedes modificar este grafo para probar diferentes escenarios.
# Asegúrate de que los pesos de las aristas no sean negativos para Dijkstra.
# Este grafo es no dirigido, es decir, si hay una arista A-B con peso X,
# entonces hay una conexión de A a B y de B a A con el mismo peso.
example_graph = { # Define un grafo de ejemplo.
    'A': {'B': 4, 'C': 2}, # Nodo A con conexiones a B (peso 4) y C (peso 2).
    'B': {'A': 4, 'E': 3}, # Nodo B con conexiones a A (peso 4) y E (peso 3).
    'C': {'A': 2, 'D': 2, 'E': 5}, # Nodo C con conexiones a A (2), D (2) y E (5).
    'D': {'C': 2, 'E': 1}, # Nodo D con conexiones a C (2) y E (1).
    'E': {'B': 3, 'C': 5, 'D': 1} # Nodo E con conexiones a B (3), C (5) y D (1).
}

# --- NODO DE INICIO ---
# Puedes cambiar este nodo para iniciar la simulación desde otro punto.
example_start_node = 'A' # Define el nodo de inicio para la simulación.

# Ejecutar la simulación
dijkstra_simulation(example_graph, example_start_node) # Llama a la función de simulación con el grafo y el nodo de inicio.