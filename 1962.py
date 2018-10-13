N = int(input())
anos = []
for i in range(N):
    T = int(input())
    A = 2015 - T
    if A < 0:
        A -= 1
    anos.append(A)
for ano in anos:
    if ano == 0: print("1 A.C.")
    elif ano > 0:
        print("{} D.C.".format(ano))
    else:
        print("{} A.C.".format(ano * -1))
