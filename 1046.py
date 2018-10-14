inicio, fim = map(int, input().split())

duracao = fim - inicio
if duracao <= 0: duracao += 24

print("O JOGO DUROU {} HORA(S)".format(duracao))
