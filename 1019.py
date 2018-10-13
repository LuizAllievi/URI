N = int(input())

segundos = N % 60
N = N // 60
minutos = N % 60
N = N // 60
horas = N

print("{}:{}:{}".format(horas, minutos, segundos))
