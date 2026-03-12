def resolver_problema():
    n = int(input())
    eventos = list(map(int, input().split()))

    policias_disponibles = 0
    crimenes_sin_resolver = 0

    for evento in eventos:
        if evento > 0:
            policias_disponibles += evento
        else:
            if policias_disponibles > 0:
                policias_disponibles -= 1
            else:
                crimenes_sin_resolver += 1

    print(crimenes_sin_resolver)

if __name__ == "__main__":
    resolver_problema()