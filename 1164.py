N = int(input())

vetor = []
for i in range(N):
    X = int(input())
    soma = 0
    for numero in range(1, X):
        if X % numero == 0:
            soma += numero
    vetor.append((X, soma))

for item in vetor:
    if item[0] == item[1]:
        print("{} eh perfeito".format(item[0]))
    else:
        print("{} nao eh perfeito".format(item[0]))
