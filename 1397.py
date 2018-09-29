partidas = []
while True:
    N = int(input())
    p_1 = 0
    p_2 = 0
    if N == 0: break
    for i in range(N):
        A, B = map(int, input().split())
        if A > B: p_1 += 1
        elif B > A: p_2 += 1
    partidas.append((p_1, p_2))
for i in partidas:
    print("{} {}".format(i[0], i[1]))

    
