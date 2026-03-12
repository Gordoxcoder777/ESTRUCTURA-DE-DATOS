def resolver_problema():
    d1, d2, d3 = map(int, input().split())

    ruta1 = d1 + d3 + d2
    ruta2 = 2 * (d1 + d2)
    ruta3 = 2 * (d1 + d3)
    ruta4 = 2 * (d2 + d3)

    print(min(ruta1, ruta2, ruta3, ruta4))


resolver_problema()