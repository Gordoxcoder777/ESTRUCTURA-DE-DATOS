q = int(input())

for _ in range(q):
    n = int(input())
    moves = 0
    
    while n != 1:
        if n % 2 == 0:
            n //= 2
            moves += 1
        elif n % 3 == 0:
            n = (2 * n) // 3
            moves += 1
        elif n % 5 == 0:
            n = (4 * n) // 5
            moves += 1
        else:
            moves = -1
            break
    
    print(moves)