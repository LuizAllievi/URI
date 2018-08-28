# -*- coding: utf-8 -*-
from heapq import *
def add_prioridade(list_prio, mat_ares , vert_atual):
    for elem in mat_ares[vert_atual]:
        print(elem)
        heappush(list_prio, elem)
    return(list_prio, mat_ares, vert_atual)

def main():
    print(1)

    vertices, arestas = map(int, input().split())
    matriz_arestas = [[] for i in range(vertices)]

    #Populando a matriz de entradas
    for x in range(arestas):
        origem, destino, distancia = map(int, input().split())
        matriz_arestas[origem].append([distancia, destino])

    input()
    #=================================================================

    lista_prioridade = []
    visitados = [False for i in range(vertices)]
    vertice_atual = 0


    add_prioridade(lista_prioridade, matriz_arestas, vertice_atual)
    visitados[vertice_atual] = True
    soma_menor_caminho = 0

    print(lista_prioridade)
    input()
    while lista_prioridade and (not all(visitados)):
        peso, destino = heappop(lista_prioridade)
        visitados[destino] = True

        lista_prioridade, matriz_arestas, vertice_atual = add_prioridade(lista_prioridade, matriz_arestas, vertice_atual)

        print(matriz_arestas)
        print(lista_prioridade)

if __name__ == '__main__':
    main()
