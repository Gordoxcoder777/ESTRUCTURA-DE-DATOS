n = int(input())
t = input()

result = ""
i = 0
step = 1

while i < n:
    result += t[i]
    i += step
    step += 1

print(result)