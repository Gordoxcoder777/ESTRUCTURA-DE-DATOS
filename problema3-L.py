first, last = input().split()

result = first[0]

for c in first[1:]:
    if c < last[0]:
        result += c
    else:
        break

result += last[0]

print(result)