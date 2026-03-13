# Leer tamaño de la permutación
n = int(input())

# Leer permutación
p = list(map(int, input().split()))

# Leer matriz de adyacencia
A = [input().strip() for _ in range(n)]

# Lista de visitados para DFS
visited = [False] * n


# DFS para encontrar componentes conectados
def dfs(i, comp):

    visited[i] = True      # marcamos nodo visitado
    comp.append(i)         # añadimos nodo al componente

    # revisamos conexiones
    for j in range(n):

        # si hay conexión y no fue visitado
        if A[i][j] == '1' and not visited[j]:

            dfs(j, comp)


# recorrer todos los nodos
for i in range(n):

    if not visited[i]:

        comp = []

        # encontrar componente conectado
        dfs(i, comp)

        # valores de la permutación en ese componente
        values = [p[x] for x in comp]

        # ordenar posiciones y valores
        comp.sort()
        values.sort()

        # colocar los valores ordenados en las posiciones
        for k in range(len(comp)):
            p[comp[k]] = values[k]


# imprimir resultado
print(*p)