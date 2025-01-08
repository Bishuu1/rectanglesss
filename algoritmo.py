def CalcularRectangulos(x, y, a, b, memo=None):
    ''' Función para calcular cuantos rectangulos de tamaño a*b caben en el rectangulo de tamaño x*y '''
    if x < 0 or y < 0 or a < 0 or b < 0:  # Se verifica que los valores sean positivos
        return 0
    # Se ordenan los valores asumiendo que no estan necesariamente ordenados, tal que y = largoTecho e b = largoPanel
    x, y = sorted([x, y])
    a, b = sorted([a, b])
    if memo is None:
        memo = {}
    # Se verifica que los paneles no sean más grandes que el techo
    if (a > x and b > x) or (a > y and b > y):
        return 0
    if (x, y) in memo:
        return memo[(x, y)]
    best1 = 0
    best2 = 0
    if a <= x and b <= y:
        best1 = 1 + CalcularRectangulos(x - a, b, a, b, memo) + \
            CalcularRectangulos(x, y - b, a, b, memo)
        best2 = 1 + CalcularRectangulos(x - a, y, a, b, memo) + \
            CalcularRectangulos(a, y - b, a, b, memo)
    best3 = 0
    best4 = 0
    if b <= x and a <= y:
        best3 = 1 + CalcularRectangulos(x - b, a, a, b, memo) + \
            CalcularRectangulos(x, y - a, a, b, memo)
        best4 = 1 + CalcularRectangulos(x - b, y, a, b, memo) + \
            CalcularRectangulos(b, y - a, a, b, memo)
    best = max(best1, best2, best3, best4)
    memo[(x, y)] = best
    return best


if __name__ == "__main__":
    entrada = input("Ingrese x, y, a, b separados por espacios: ")
    x, y, a, b = map(int, entrada.split())
    resultado = CalcularRectangulos(x, y, a, b)
    print(
        f"\nMáximo número de paneles {a}*{b} que caben en {x}*{y}: {resultado}")
