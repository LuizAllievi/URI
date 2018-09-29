N = int(input())
i = 0
cedulas = [100, 50, 20, 10, 5, 2, 1]
print("{}".format(N))
while i < 7:
    print("{} nota(s) de R$ {},00".format(N // cedulas[i], cedulas[i]))
    N = N % cedulas[i]
    i += 1
    
