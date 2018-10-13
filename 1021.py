dinheiro = float(input())
dinheiro += 0.001
notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    quantidade_notas = dinheiro // nota
    dinheiro = dinheiro % nota
    print("{:d} nota(s) de R$ {:.2f}".format(int(quantidade_notas), nota))

print("MOEDAS:")
for moeda in moedas:
    quantidade_moedas = dinheiro // moeda
    dinheiro = dinheiro % moeda
    print("{:d} moeda(s) de R$ {:.2f}".format(int(quantidade_moedas), moeda))
