from collections import deque
import sys

base_deck = [str(i) for i in range(1, 51)]

for line in sys.stdin:
    n = line.strip()

    if not n.isdigit():
        continue

    if n == "0":
        break

    deck = deque()
    for card in base_deck:
        deck.append(card)
        if card == n:
            break

    discarded = []

    while len(deck) > 1:
        discarded.append(deck.popleft())
        deck.append(deck.popleft())

    print("Discarded cards:", end="")
    if discarded:
        print(" " + ", ".join(discarded))
    else:
        print()
    print("Remaining card:", deck[0])