tempo = int(input())
velocidade_media = int(input())
consumo = 12

distancia = velocidade_media * tempo

litros = distancia / consumo

print("{:.3f}".format(litros))
