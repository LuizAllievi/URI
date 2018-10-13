combustiveis = [0, 0, 0]

entrada = int(input())
while entrada != 4:
    if entrada in [1, 2, 3]:
        combustiveis[entrada - 1] += 1
    entrada = int(input())

print("MUITO OBRIGADO")
print("Alcool: {}".format(combustiveis[0]))
print("Gasolina: {}".format(combustiveis[1]))
print("Diesel: {}".format(combustiveis[2]))
