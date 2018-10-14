inicio_hora, inicio_minuto, fim_hora, fim_minuto = map(int, input().split())

minutos_inicio = inicio_hora * 60 + inicio_minuto
minutos_fim = fim_hora * 60 + fim_minuto

tempo_jogo = minutos_fim - minutos_inicio

tempo_hora = tempo_jogo // 60
tempo_minuto = tempo_jogo % 60

if tempo_hora < 0 or (tempo_hora == 0 and tempo_minuto == 0):
    tempo_hora += 24


print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(tempo_hora, tempo_minuto))
