import sys

def tokenize(s):
    """Convierte el string en una lista de tokens: '(', ')' o números."""
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in '()':
            tokens.append(s[i])
            i += 1
        elif s[i].isdigit() or (s[i] == '-' and i + 1 < len(s) and s[i+1].isdigit()):
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            tokens.append(int(s[i:j]))
            i = j
        else:
            i += 1  # saltar espacios y saltos de línea
    return tokens

def parse(tokens, idx):
    """
    Parsea recursivamente el árbol desde tokens[idx].
    Retorna (nodo, nuevo_idx).
    Nodo puede ser None (árbol vacío) o (valor, izq, der).
    """
    # Debe empezar con '('
    idx += 1  # consumir '('

    if tokens[idx] == ')':
        # Árbol vacío: ()
        return None, idx + 1

    # Árbol con valor: (entero árbol_izq árbol_der)
    value = tokens[idx]
    idx += 1

    left, idx = parse(tokens, idx)
    right, idx = parse(tokens, idx)

    idx += 1  # consumir ')'
    return (value, left, right), idx

def has_path_sum(node, target, current_sum):
    """
    Verifica si existe un camino raíz-hoja cuya suma sea igual a target.
    """
    if node is None:
        return False

    value, left, right = node
    current_sum += value

    # Es hoja si ambos hijos son None
    if left is None and right is None:
        return current_sum == target

    return has_path_sum(left, target, current_sum) or \
           has_path_sum(right, target, current_sum)

def main():
    data = sys.stdin.read()
    tokens = tokenize(data)

    idx = 0
    while idx < len(tokens):
        # Leer el entero objetivo
        target = tokens[idx]
        idx += 1

        # Parsear el árbol
        tree, idx = parse(tokens, idx)

        # Verificar si existe el camino
        if has_path_sum(tree, target, 0):
            print("yes")
        else:
            print("no")

main()