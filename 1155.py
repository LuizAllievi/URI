# -*- coding: utf-8 -*-
# Luiz Allievi
# Sequencia S

def sequencia_s(n):
    if n == 100:
        return(1/n)
    else:
        return (1/n + sequencia_s(n + 1))

result = sequencia_s(1)
print("{}".format(round(result, 2)))
