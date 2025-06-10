class Node:
    def __init__(self, key):  # Constructor de la clase Node, recibe la clave del nodo
        self.key = key        # Asigna el valor de la clave al nodo
        self.left = None      # Inicializa el hijo izquierdo como None
        self.right = None     # Inicializa el hijo derecho como None

def insert(root, key):
    # Si el nodo raíz es None, crea un nuevo nodo con la clave y lo retorna
    if root is None:
        return Node(key)
    # Si la clave es menor que la clave del nodo raíz, inserta en el subárbol izquierdo
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        # Si la clave es mayor o igual, inserta en el subárbol derecho
        root.right = insert(root.right, key)
    # Retorna el nodo raíz actualizado
    return root

def inorder_traversal(root, result):
    if root:  # Si el nodo actual no es None
        inorder_traversal(root.left, result)  # Recorre recursivamente el subárbol izquierdo
        result.append(root.key)  # Agrega la clave del nodo actual a la lista de resultados
        inorder_traversal(root.right, result)  # Recorre recursivamente el subárbol derecho

def tree_sort(arr):
    # Si la lista está vacía, retorna una lista vacía
    if not arr:
        return []
    root = None  # Inicializa la raíz del árbol como None
    for key in arr:
        root = insert(root, key)  # Inserta cada elemento de la lista en el árbol
    result = []  # Lista para almacenar el recorrido en orden
    inorder_traversal(root, result)  # Realiza el recorrido en orden y llena la lista resultado
    return result  # Retorna la lista ordenada

# Ejemplo de uso
if __name__ == "__main__":
    datos = [5, 3, 7, 2, 4, 6, 8]
    print("Lista original:", datos)
    ordenada = tree_sort(datos)
    print("Lista ordenada:", ordenada)