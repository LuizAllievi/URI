a, b, c = map(int, input().split())

A = a
B = b
C = c

if (b > c):
    aux = c
    c = b
    b = aux
if (a > b):
    aux = b
    b = a
    a = aux
if (b > c):
    aux = c
    c = b
    b = aux

for numero in [a, b, c, "", A, B, C]:
    print("{}".format(numero))
