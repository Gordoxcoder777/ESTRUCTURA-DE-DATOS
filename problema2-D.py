n, t = map(int, input().split())
a = list(map(int, input().split()))

pos = 1

while pos < t:
    pos = pos + a[pos - 1]

if pos == t:
    print("YES")
else:
    print("NO")