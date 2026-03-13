q = int(input())

for _ in range(q):
    n = int(input())
    arr = list(map(int, input().split()))
    
    total = 0
    
    for x in arr:
        if x <= 2048:
            total += x
    
    if total >= 2048:
        print("YES")
    else:
        print("NO")