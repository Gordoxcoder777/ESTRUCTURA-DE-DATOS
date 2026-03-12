import sys

def solve(source, target):
    results = [] 
   def backtrack(src_idx, tgt_idx, stack, sequence):

        if tgt_idx == len(target):
            if src_idx == len(source) and len(stack) == 0:
                results.append(sequence[:])  # Guardamos copia de la secuencia
            return

        if src_idx < len(source):
            sequence.append('i')
            stack.append(source[src_idx])
            backtrack(src_idx + 1, tgt_idx, stack, sequence)
            sequence.pop()
            stack.pop()

        if stack:
            top = stack[-1]
            if top == target[tgt_idx]:
                sequence.append('o')
                stack.pop()
                backtrack(src_idx, tgt_idx + 1, stack, sequence)
                sequence.append... 
                stack.append(top)
                sequence.pop()

    backtrack(0, 0, [], [])
    return results

lines = sys.stdin.read().splitlines()
i = 0
while i < len(lines) - 1:
    source = lines[i].strip()
    target = lines[i+1].strip()
    i += 2

    print('[')

    if len(source) == len(target):
        seqs = solve(source, target)
        for seq in seqs:
            print(' '.join(seq))

    print(']')