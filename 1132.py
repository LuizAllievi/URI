X  = int(input())
Y = int(input())

soma = 0

maior = X if X > Y else Y
menor = Y if X > Y else X


for i in range(menor, maior + 1):
    if i % 13 != 0:
        soma += i

print("{}".format(soma))
