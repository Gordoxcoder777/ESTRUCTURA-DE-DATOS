import sys
from sys import setrecursionlimit
input = sys.stdin.readline
setrecursionlimit(200000)

def solve():
    n = int(input())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)

    expected = 0.0

    # DFS iterativo para evitar recursión profunda con n=100000
    # stack: (nodo_actual, padre, probabilidad_de_llegar_aqui)
    stack = [(1, 0, 1.0)]

    while stack:
        node, parent, prob = stack.pop()

        # Hijos = vecinos excluyendo el padre
        children = [v for v in adj[node] if v != parent]

        if not children:
            # Nodo hoja: el recorrido termina aquí, no suma más
            continue

        k = len(children)
        # Cada arista hacia un hijo contribuye con prob / k al valor esperado
        for child in children:
            child_prob = prob / k
            expected += child_prob   # arista de longitud 1 tomada con prob child_prob
            stack.append((child, node, child_prob))

    print(f"{expected:.15f}")

solve()