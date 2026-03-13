q = int(input())

for _ in range(q):
    a, b, c = map(int, input().split())
    
    ans = float('inf')
    
    for da in [-1, 0, 1]:
        for db in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                na = a + da
                nb = b + db
                nc = c + dc
                
                dist = abs(na - nb) + abs(na - nc) + abs(nb - nc)
                
                ans = min(ans, dist)
    
    print(ans)