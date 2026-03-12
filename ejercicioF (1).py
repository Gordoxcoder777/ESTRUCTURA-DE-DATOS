s = input().strip()
numeros = s.split('+')
numeros.sort()
print('+'.join(numeros))