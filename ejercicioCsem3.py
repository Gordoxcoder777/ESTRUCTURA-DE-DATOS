num=int(input())
lista=list(map(int,input().split()))
save=[]
for i in lista:
    save.append(lista.count(i))
print (max(save))