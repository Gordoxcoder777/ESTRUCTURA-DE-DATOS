n = int(input())
h = list(map(int, input().split()))

ans = 0

for i in range(n):
    left = i
    right = i

    while left > 0 and h[left - 1] <= h[left]:
        left -= 1

    while right < n - 1 and h[right + 1] <= h[right]:
        right += 1

    ans = max(ans, right - left + 1)

print(ans)