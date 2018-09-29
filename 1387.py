L, R = 1, 1
Ll = []
Rl = []
while True:
    L, R = map(int, input().split())
    if L == R == 0: break
    Ll.append(L)
    Rl.append(R)

for i in range(len(Ll)):
    print("{}".format(Ll[i] + Rl[i]))
