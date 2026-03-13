primero = True

while True:
    try:
        n = int(input())
    except:
        break

    if not primero:
        print()  # Solo imprime línea en blanco si NO es el primer grupo
    primero = False

    nombres = input().split()
    balance = {}

    for nombre in nombres:
        balance[nombre] = 0

    for _ in range(n):
        datos = input().split()
        nombre = datos[0]
        dinero_total = int(datos[1])
        cantidad = int(datos[2])

        if cantidad == 0:
            continue

        dinero_por_persona = dinero_total // cantidad
        dinero_entregado = dinero_por_persona * cantidad

        balance[nombre] -= dinero_entregado

        for i in range(3, 3 + cantidad):
            amigo = datos[i]
            balance[amigo] += dinero_por_persona

    for nombre in nombres:
        print(nombre, balance[nombre])