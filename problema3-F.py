t = int(input())

for _ in range(t):
    n = input().strip()
    d = len(n)
    
    first_digit = int(n[0])
    
    result = (d - 1) * 9 + first_digit
    
    if int(n) < int(n[0] * d):
        result -= 1
    
    print(result)