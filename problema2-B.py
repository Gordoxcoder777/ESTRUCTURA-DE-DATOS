n, m = map(int, input().split())
a = list(map(int, input().split()))

max_turns = 0
last_child = 0

for i in range(n):
    turns = (a[i] + m - 1) // m
    if turns >= max_turns:
        max_turns = turns
        last_child = i + 1

print(last_child)