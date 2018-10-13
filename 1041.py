x, y = map(float, input().split())

if (x == y == 0):
    print("Origem")

elif (x > 0):
    if (y > 0):
        print("Q1")
    elif (y < 0):
        print("Q4")
    else:
        print("Eixo X")

elif (x < 0):
    if (y > 0):
        print("Q2")
    elif (y < 0):
        print("Q3")
    else:
        print("Eixo X")

else:
    print ("Eixo Y")
