# -*- coding: utf-8 -*-

A, B, C = map(int, input().split())


if ((A == B) or (B == C) or (A == C)):
    print("{}".format("S"))
elif (((A + B) == C) or ((A + C) == B) or ((B + C) == A)):
    print("{}".format("S"))
else:
    print("{}".format("N"))
