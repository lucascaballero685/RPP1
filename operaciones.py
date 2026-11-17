def sumar_vector(vector):
    total = 0
    for i in range(len(vector)):
        total += vector[i]
    return total

def obtener_maximo(vector):
    if len(vector) == 0:
        return None
    max_val = vector[0]
    for i in range(1, len(vector)):
        if vector[i] > max_val:
            max_val = vector[i]
    return max_val