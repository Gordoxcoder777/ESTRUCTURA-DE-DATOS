guest = input().strip()
host = input().strip()
pile = input().strip()

if sorted(guest + host) == sorted(pile):
    print("YES")
else:
    print("NO")