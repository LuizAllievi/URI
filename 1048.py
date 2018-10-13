salario = float(input())

if (salario <= 400):
    taxa_reajuste = 0.15
    novo_salario = salario + salario * taxa_reajuste
    reajuste = novo_salario - salario
elif (salario <= 800):
    taxa_reajuste = 0.12
    novo_salario = salario + salario * taxa_reajuste
    reajuste = novo_salario - salario
elif (salario <= 1200):
    taxa_reajuste = 0.1
    novo_salario = salario + salario * taxa_reajuste
    reajuste = novo_salario - salario
elif (salario <= 2000):
    taxa_reajuste = 0.07
    novo_salario = salario + salario * taxa_reajuste
    reajuste = novo_salario - salario
else:
    taxa_reajuste = 0.04
    novo_salario = salario + salario * taxa_reajuste
    reajuste = novo_salario - salario

print("Novo salario: {:.2f}".format(round(novo_salario, 3)))
print("Reajuste ganho: {:.2f}".format(round(reajuste, 2)))
print("Em percentual: {:d} %".format(int(taxa_reajuste * 100)))
