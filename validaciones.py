def es_entero_positivo(cadena):
    """Valida manualmente si una cadena representa un entero positivo > 0."""
    if len(cadena) == 0:
        return False
    for i in range(len(cadena)):
        caracter = cadena[i]
        if caracter < '0' or caracter > '9':
            return False
    return True

def convertir_a_entero(cadena):
    """Convierte una cadena valida a numero entero sin usar funciones prohibidas."""
    valor = 0
    for i in range(len(cadena)):
        digito = ord(cadena[i]) - ord("0")
        valor = valor * 10 + digito
    return valor