class UnionFind:
    def __init__(self, n):
        # Inicializa el array de padres, cada nodo es su propio padre
        self.parent = list(range(n))
    
    def find(self, u):
        # Encuentra la raíz del conjunto al que pertenece u (con compresión de caminos)
        while u != self.parent[u]:
            self.parent[u] = self.parent[self.parent[u]]  # Compresión de caminos
            u = self.parent[u]
        return u
    
    def union(self, u, v):
        # Une los conjuntos de u y v, retorna False si ya están unidos
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False  # Ya están en el mismo conjunto
        self.parent[pu] = pv  # Une los conjuntos
        return True

def kruskal(edges, n, reverse=False):
    # Ordena las aristas por peso (ascendente o descendente según reverse)
    edges = sorted(edges, key=lambda x: x[2], reverse=reverse)
    uf = UnionFind(n)  # Inicializa la estructura Union-Find
    mst = []           # Lista para almacenar las aristas del árbol
    cost = 0           # Costo total del árbol
    print("\n--- Proceso de Kruskal ---")
    for u, v, w in edges:
        # Muestra la arista que se está considerando
        print(f"Considerando arista ({u}, {v}) con peso {w}...")
        if uf.union(u, v):
            # Si no forma ciclo, se añade al árbol
            mst.append((u, v, w))
            cost += w
            print(f"  -> Añadida al árbol. Costo actual: {cost}")
        else:
            # Si forma ciclo, se descarta
            print(f"  -> Descartada (formaría ciclo).")
        if len(mst) == n - 1:
            # Si ya se tienen n-1 aristas, se termina
            break
    print(f"Árbol {'Máximo' if reverse else 'Mínimo'} encontrado: {mst}")
    print(f"Costo total: {cost}\n")
    return mst, cost

# Ejemplo de uso
# Definir el grafo: lista de aristas (u, v, peso)
edges = [
    (0, 1, 4),   # Arista entre nodo 0 y 1 con peso 4
    (0, 2, 3),   # Arista entre nodo 0 y 2 con peso 3
    (1, 2, 1),   # Arista entre nodo 1 y 2 con peso 1
    (1, 3, 2),   # Arista entre nodo 1 y 3 con peso 2
    (2, 3, 4),   # Arista entre nodo 2 y 3 con peso 4
    (3, 4, 2),   # Arista entre nodo 3 y 4 con peso 2
    (4, 5, 6)    # Arista entre nodo 4 y 5 con peso 6
]
n = 6  # Número de nodos (0 a 5)

print("Árbol de Mínimo Coste (Kruskal):")
kruskal(edges, n, reverse=False)  # Ejecuta Kruskal para árbol de mínimo coste

print("Árbol de Máximo Coste (Kruskal):")
kruskal(edges, n, reverse=True)   # Ejecuta Kruskal para árbol de máximo coste