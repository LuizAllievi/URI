i = 0
cont = 0
while i < 5:
    entry = int(input())
    if (entry % 2) == 0:
        cont += 1
    i += 1
print("{} valores pares".format(cont))
