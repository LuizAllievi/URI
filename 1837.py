# -*- coding: utf-8 -*-

a, b = map(int, input().split())

if (a < 0):
    e = b;
    if ( b < 0):
        e = b * -1
    for r in range(e):
        f = a - r
        if (f % b == 0): break
    q = f / b
else:
    q = a / b
    r = a % b

print("{}{}".format(q, r))
