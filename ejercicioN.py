import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    target = n // 3

    # Contar cuántos elementos tienen cada resto
    c = [0, 0, 0]
    for x in a:
        c[x % 3] += 1

    moves = 0

    # Pasar excesos en orden 0->1->2->0
    # Hacemos 2 vueltas para manejar el ciclo (ej: exceso en 2 que va a 0)
    for _ in range(2):
        for r in range(3):
            nxt = (r + 1) % 3
            if c[r] > target:
                excess = c[r] - target
                moves += excess          # cada elemento necesita 1 incremento
                c[r] -= excess
                c[nxt] += excess

    print(moves)

t = int(input())
for _ in range(t):
    solve()