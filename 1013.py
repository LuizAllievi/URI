A, B, C = map(int, input().split())

maiorAB = (A + B + abs(A - B)) / 2

maiorC = (maiorAB + C + abs(maiorAB - C)) / 2

print("{:.0f} eh o maior".format(maiorC))
