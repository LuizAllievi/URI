# -*- coding: utf-8 -*-
A, B, C = map(float, input().split())

if (A>=B>=C):
    a = A
    b = B
    c = C
elif (A>=C>=B):
    a = A
    b = C
    c = B
elif (B>=A>=C):
    a = B
    b = A
    c = C
elif (B>=C>=A):
    a = B
    b = C
    c = A
elif (C>=A>=B):
    a = C
    b = A
    c = B
elif (C>=B>=A):
    a = C
    b = B
    c = A


# URI Conditions
if (a >= (b + c)):
    print("{}".format("NAO FORMA TRIANGULO"))
elif (a * a == (b * b + c * c)):
    print("{}".format("TRIANGULO RETANGULO"))
elif (a * a > (b * b + c * c)):
    print("{}".format("TRIANGULO OBTUSANGULO"))
elif (a * a < (b * b + c * c)):
    print("{}".format("TRIANGULO ACUTANGULO"))
if (a == b and b == c):
    print("{}".format("TRIANGULO EQUILATERO"))
elif ((a == b) or (a == c) or (b == c)):
    print("{}".format("TRIANGULO ISOSCELES"))
