import sys
input = sys.stdin.readline

def post_order(preorder):
    """
    Dado el pre-order de un BST, imprime el post-order
    sin construir explícitamente el árbol.
    
    Enfoque recursivo directo:
    - preorder[0] es la raíz
    - Los elementos < raíz forman el subárbol izquierdo
    - Los elementos > raíz forman el subárbol derecho
    - Post-order: izquierda, derecha, raíz
    """
    if not preorder:
        return

    root = preorder[0]
    rest = preorder[1:]

    # Encontrar el límite entre subárbol izquierdo y derecho
    split = 0
    while split < len(rest) and rest[split] < root:
        split += 1

    left  = rest[:split]   # todos menores que root
    right = rest[split:]   # todos mayores que root

    # Post-order: izquierda -> derecha -> raíz
    post_order(left)
    post_order(right)
    print(root)

def main():
    data = sys.stdin.read().split()
    preorder = list(map(int, data))
    sys.setrecursionlimit(20000)
    post_order(preorder)

main()