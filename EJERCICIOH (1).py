import sys

def solve(source, target):
    results = []

    def backtrack(src_idx, tgt_idx, stack, sequence):
        if tgt_idx == len(target) and src_idx == len(source) and len(stack) == 0:
            results.append(sequence[:])
            return

        if tgt_idx > len(target) or src_idx > len(source):
            return
        if src_idx < len(source):
            stack.append(source[src_idx])
            sequence.append('i')
            backtrack(src_idx + 1, tgt_idx, stack, sequence)
            sequence.pop()
            stack.pop()

        if stack and tgt_idx < len(target) and stack[-1] == target[tgt_idx]:
            top = stack.pop()
            sequence.append('o')
            backtrack(src_idx, tgt_idx + 1, stack, sequence)
            sequence.pop()
            stack.append(top)  

    backtrack(0, 0, [], [])
    return results

lines = sys.stdin.read().splitlines()
i = 0
while i < len(lines) - 1:
    source = lines[i].strip()
    target = lines[i + 1].strip()
    i += 2

    print('[')
    if len(source) == len(target):
        for seq in solve(source, target):
            print(' '.join(seq))
    print(']')