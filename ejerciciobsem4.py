t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    vistos = set()
    p = []
    
    for x in a:
        if x not in vistos:
            p.append(x)
            vistos.add(x)
    
    print(*p)