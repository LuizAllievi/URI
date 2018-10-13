A, B, C = map(float, input().split())

delta = (B ** 2 - (4 * A * C))

if (A == 0) or (delta <= 0):
    print("Impossivel calcular")
else:
    raiz_delta = delta ** (1 / 2)
    divisor = 2 * A
    R1 = (-B + raiz_delta) / divisor
    R2 = (-B - raiz_delta) / divisor

    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))
