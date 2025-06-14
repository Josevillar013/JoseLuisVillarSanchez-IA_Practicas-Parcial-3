import sys
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class CalculadoraMST:
    """
    Una clase para encontrar y visualizar el Árbol de Expansión Mínima (MST)
    de un grafo usando el algoritmo de Prim con una cola de prioridad.
    """
    def __init__(self, matriz_adyacencia):
        """
        Inicializa la calculadora con la matriz de adyacencia del grafo.
        """
        self.matriz = matriz_adyacencia
        self.num_vertices = len(matriz_adyacencia)
        self.nombres_nodos = list(range(self.num_vertices))

    def encontrar_mst_prim(self, nodo_inicial=0):
        """
        Encuentra el MST usando el algoritmo de Prim.

        Utiliza una cola de prioridad (min-heap) para seleccionar eficientemente
        la siguiente arista con el menor peso a agregar al árbol.
        """
        # La cola de prioridad almacenará tuplas de (peso, nodo_origen, nodo_destino)
        cola_prioridad = []
        
        # Conjunto para rastrear los vértices ya incluidos en el MST
        visitados = set()
        
        # Aristas que formarán el MST final y su costo total
        aristas_mst = []
        costo_total = 0

        # Empezamos desde el nodo inicial
        # El primer elemento no tiene origen (-1) y su peso es 0 para que sea el primero en ser procesado
        heapq.heappush(cola_prioridad, (0, nodo_inicial, -1))

        while cola_prioridad and len(visitados) < self.num_vertices:
            peso, nodo_actual, nodo_origen = heapq.heappop(cola_prioridad)

            # Si el nodo ya fue visitado, lo ignoramos y continuamos
            if nodo_actual in visitados:
                continue

            # Agregamos el nuevo nodo al conjunto de visitados
            visitados.add(nodo_actual)

            # Si no es el nodo de partida, agregamos la arista al MST
            if nodo_origen != -1:
                aristas_mst.append((nodo_origen, nodo_actual, peso))
                costo_total += peso

            # Exploramos los vecinos del nodo actual
            for vecino, peso_arista in enumerate(self.matriz[nodo_actual]):
                # Si hay una conexión (peso != 0) y el vecino no ha sido visitado
                if peso_arista > 0 and vecino not in visitados:
                    # Agregamos la arista a la cola de prioridad
                    heapq.heappush(cola_prioridad, (peso_arista, vecino, nodo_actual))
        
        return aristas_mst, costo_total

    def visualizar_grafo_y_mst(self, aristas_mst):
        """
        Crea una visualización del grafo completo con el MST resaltado.
        """
        G = nx.Graph()

        # Agregar todas las aristas del grafo original
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices):
                if self.matriz[i][j] > 0:
                    G.add_edge(i, j, weight=self.matriz[i][j])

        pos = nx.spring_layout(G, seed=42)  # Layout consistente
        plt.figure(figsize=(10, 8))

        # Dibujar el grafo base
        nx.draw(
            G, pos, with_labels=True, node_color='skyblue', 
            node_size=2500, font_size=11, font_weight='bold', edge_color='lightgray'
        )

        # Resaltar las aristas del MST
        nx.draw_networkx_edges(
            G, pos, edgelist=[(u, v) for u, v, w in aristas_mst], 
            edge_color='red', width=2.5
        )

        # Etiquetas de peso para todas las aristas
        etiquetas_pesos = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_pesos)

        plt.title("Visualización del Grafo con MST Resaltado", size=16)
        plt.show()

def ejecutar_demostracion():
    """
    Función principal para ejecutar la demostración del cálculo de MST.
    """
    # Matriz de adyacencia que representa el grafo
    grafo_matriz = [
        [0, 4, 6, 0, 0, 0],
        [4, 0, 6, 3, 4, 0],
        [6, 6, 0, 1, 8, 0],
        [0, 3, 1, 0, 2, 3],
        [0, 4, 8, 2, 0, 7],
        [0, 0, 0, 3, 7, 0]
    ]

    # Crear una instancia de la calculadora
    calculadora = CalculadoraMST(grafo_matriz)
    
    # Encontrar el MST y su costo
    aristas_del_mst, costo_del_mst = calculadora.encontrar_mst_prim()

    # Imprimir los resultados en la consola
    print("--- Árbol de Expansión Mínima (MST) Encontrado ---")
    for origen, destino, peso in aristas_del_mst:
        print(f'  Arista: {origen} -> {destino}   |   Peso: {peso}')
    print(f"Costo total del MST: {costo_del_mst}")
    print("-------------------------------------------------")

    # Mostrar la visualización gráfica
    calculadora.visualizar_grafo_y_mst(aristas_del_mst)

# Punto de entrada del script
if __name__ == "__main__":
    ejecutar_demostracion()