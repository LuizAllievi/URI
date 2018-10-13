numero = float(input())

if (25 >= numero >= 0):
    print("Intervalo [0,25]")
elif (50 >= numero > 25 ):
    print("Intervalo (25,50]")
elif (75 >= numero > 50):
    print("Intervalo (50,75]")
elif (100 >= numero > 75):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
