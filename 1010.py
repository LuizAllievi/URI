total = 0
for i in range(2):
    codigo, quantidade, valor = map(float, input().split())
    total += quantidade * valor


print("VALOR A PAGAR: R$ {:.2F}".format(total))
