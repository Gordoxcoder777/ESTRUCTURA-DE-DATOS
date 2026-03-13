def resolver_problema():
    n = int(input().strip())
    eventos = input().split()

    policias = 0
    sin_resolver = 0

    for e in eventos:
        if e == "-1":
            if policias > 0:
                policias -= 1
            else:
                sin_resolver += 1
        else:
            policias += int(e)

    print(sin_resolver)


resolver_problema()