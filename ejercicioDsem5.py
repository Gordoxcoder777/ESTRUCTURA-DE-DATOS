n = int(input())
a = list(map(int, input().split()))

stairs = []
for i in range(1, n):
    if a[i] == 1:
        stairs.append(a[i-1])  # la escalera anterior terminó aquí

stairs.append(a[-1])  # última escalera

print(len(stairs))
print(*stairs)