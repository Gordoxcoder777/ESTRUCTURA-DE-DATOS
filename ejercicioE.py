import sys

input_data = sys.stdin.read().split('\n')
line_idx = 0
output = []

while line_idx < len(input_data):
    line = input_data[line_idx].strip()
    line_idx += 1

    if not line or line == '0':
        break

    n = int(line)
    block_results = []

    while line_idx < len(input_data):
        line = input_data[line_idx].strip()
        line_idx += 1

        if not line or line == '0':
            break

        target = list(map(int, line.split()))

        stack = []          # La estación (pila)
        next_train = 1      # Próximo vagón que llega desde A
        possible = True

        for wagon in target:
            while (not stack or stack[-1] != wagon) and next_train <= n:
                stack.append(next_train)
                next_train += 1

            if stack and stack[-1] == wagon:
                stack.pop()
            else:
                possible = False
                break

        block_results.append("Yes" if possible else "No")

    output.append('\n'.join(block_results))

print('\n\n'.join(output))