n = int(input())
a = [int(input()) for _ in range(n)]

possible = False

for mask in range(1 << n):
    total = 0
    for i in range(n):
        if mask & (1 << i):
            total += a[i]
        else:
            total -= a[i]
    if total % 360 == 0:
        possible = True
        break

if possible:
    print("YES")
else:
    print("NO")