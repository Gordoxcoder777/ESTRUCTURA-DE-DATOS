def resolver_problema_b():
    linea1 = list(map(int, input().split()))
    n = linea1[0]
    m = linea1[1]
precios = list(map(int, input().split()))

    precios.sort()

    ganancias = 0

    for i in range(m):
        if precios[i] < 0:
           ganancias -= precios[i]
        else:
            break

    print(ganancias)

if __name__ == "__main__":
    resolver_problema_b()