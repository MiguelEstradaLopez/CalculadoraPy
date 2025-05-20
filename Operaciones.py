def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return None
    return a / b

def potencia(base, exponente):
    return base ** exponente

def comparar(a, b):
    if a > b:
        return f"{a} es mayor que {b}"
    elif b > a:
        return f"{b} es mayor que {a}"
    else:
        return "Ambos valores son iguales"

def mcd(a, b):
    # Algoritmo de Euclides para el máximo común divisor
    a, b = abs(int(a)), abs(int(b))
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    # Mínimo común múltiplo usando mcd
    a, b = abs(int(a)), abs(int(b))
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)