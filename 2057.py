# -*- coding: utf-8 -*-

A, B, C = list(map(int, input().split()))

hora_chegada = A + B + C


if hora_chegada >= 24:
    hora_chegada = hora_chegada - 24
elif hora_chegada < 0:
    hora_chegada = hora_chegada + 24

print("{}".format(hora_chegada))
