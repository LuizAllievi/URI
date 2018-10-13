entrada = 1
resultados = []
while entrada != 0:
    entrada = int(input())
    if not entrada: break
    resultado = [0, 0]
    if not entrada: break
    lista = list(map(int, input().split(" ")))
    for ent in lista:
        if not ent:
            resultado[0] += 1
        else:
            resultado[1] += 1
    resultados.append(resultado)

for resultado in resultados:
    print("Mary won {} times and John won {} times".format(resultado[0], resultado[1]))
