n = int(input())

skills = list(map(int, input().split()))

skills.sort()

total = 0

for i in range(0, n, 2):
    total += skills[i+1] - skills[i]

print(total)