posicao = int(input())
n1 = 0
n2 = 1
i = 2
string = "0 1"
if posicao == 1:
    print("{}".format(n1))
elif posicao == 2:
    print("{}".format(n2))
while i < posicao:
    x = n2
    n2 += n1
    n1 = x
    string += " " + str(n2)
    i += 1
print("{}".format(string))

