t = int(input())
for _ in range(t):
    a, b, c, n = map(int, input().split())
    
    total = a + b + c + n
    
    if total % 3 != 0:
        print("NO")
        continue
    
    T = total // 3
    
    if T >= a and T >= b and T >= c:
        print("YES")
    else:
        print("NO")