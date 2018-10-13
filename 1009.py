nome = input()
fixo = float(input())
comissao = float(input())

salario = fixo + (0.15 * comissao)

print("TOTAL = R$ {:.2f}".format(salario))
