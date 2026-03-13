def resolver_problema():
    n, m = map(int, input().split())
    precios = list(map(int, input().split()))

    negativos = [x for x in precios if x < 0]

    negativos.sort()

    ganancia = sum(-negativos[i] for i in range(min(m, len(negativos))))

    print(ganancia)


resolver_problema()