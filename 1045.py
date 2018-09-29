# -*- coding: utf-8 -*-
a, b, c = map(float, input().split())

if (a>=b>=c):
    A = a
    B = b
    C = c
elif (a>=c>=b):
    A = a
    B = c
    C = b
elif (b>=a>=c):
    A = b
    B = a
    C = c
elif (b>=c>=a):
    A = b
    B = c
    C = a
elif (c>=a>=b):
    A = c
    B = a
    C = b
elif (c>=b>=a):
    A = c
    B = b
    C = a


# URI Conditions
if (A >= (B + C)):
    print("{}".format("NAO FORMA TRIANGULO"))
elif (A * A == (B * B + C * C)):
    print("{}".format("TRIANGULO RETANGULO"))
elif (A * A > (B * B + C * C)):
    print("{}".format("TRIANGULO OBTUSANGULO"))
elif (A * A < (B * B + C * C)):
    print("{}".format("TRIANGULO ACUTANGULO"))
if (A == B == C):
    print("{}".format("TRIANGULO EQUILATERO"))
elif ((A == B) or (A == C) or (B == C)):
    print("{}".format("TRIANGULO ISOSCELES"))
