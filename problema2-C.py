values = {
    'Q':9,'R':5,'B':3,'N':3,'P':1,'K':0,
    'q':9,'r':5,'b':3,'n':3,'p':1,'k':0
}

white = 0
black = 0

for _ in range(8):
    row = input()
    for piece in row:
        if piece.isupper():
            white += values.get(piece,0)
        elif piece.islower():
            black += values.get(piece,0)

if white > black:
    print("White")
elif black > white:
    print("Black")
else:
    print("Draw")