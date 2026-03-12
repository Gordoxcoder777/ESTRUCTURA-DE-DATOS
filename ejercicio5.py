n = int(input())

equipos = []
for i in range(n):
    home, guest = map(int, input().split())
    equipos.append((home, guest))

conflictos = 0

for i in range(n):
    home_local = equipos[i][0]  
    
    for j in range(n):
        if i != j: 
            guest_visitante = equipos[j][1]  

            if home_local == guest_visitante:
                conflictos += 1

print(conflictos)