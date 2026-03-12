from collections import deque
import sys
input = sys.stdin.readline

def solve():
    c = int(input())
    for case in range(c):
        n, t, m = map(int, input().split())
        
        # Guardar carros con su índice original
        cars = []
        left = deque()   # (arrival_time, original_index)
        right = deque()
        
        for i in range(m):
            parts = input().split()
            arrival, bank = int(parts[0]), parts[1]
            cars.append((arrival, bank))
            if bank == 'left':
                left.append((arrival, i))
            else:
                right.append((arrival, i))
        
        results = [0] * m
        
        ferry_time = 0   # hora en que el ferry está disponible en su orilla actual
        ferry_side = 'left'
        
        remaining = m
        
        while remaining > 0:
            if ferry_side == 'left':
                current_queue = left
                other_queue = right
            else:
                current_queue = right
                other_queue = left
            
            if not current_queue and not other_queue:
                break
            
            if not current_queue:
                # No hay nadie en este lado, cruzar vacío al otro lado
                ferry_time += t
                ferry_side = 'right' if ferry_side == 'left' else 'left'
                continue
            
            # Hora de partida: el ferry espera a que llegue al menos 1 carro si no hay ninguno aún
            # (ya verificamos que current_queue no está vacía)
            depart = max(ferry_time, current_queue[0][0])
            
            # Cargar hasta n carros que hayan llegado antes o en depart
            loaded = []
            while current_queue and len(loaded) < n and current_queue[0][0] <= depart:
                loaded.append(current_queue.popleft())
            
            arrive = depart + t
            for (_, idx) in loaded:
                results[idx] = arrive
            
            remaining -= len(loaded)
            ferry_time = arrive
            ferry_side = 'right' if ferry_side == 'left' else 'left'
        
        if case > 0:
            print()
        for r in results:
            print(r)

solve()

