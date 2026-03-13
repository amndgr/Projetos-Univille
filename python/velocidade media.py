# entrada de dados
velocidade_média = float(input("Digite a velocidade média em km/h: "))
distância = float(input("Digite a distância em km: "))

# cálculo do tempo em horas
tempo = distância / velocidade_média

print("O tempo estimado é de %5.2f horas" % tempo)

# convertemos de horas para segundos
tempo_s = int(tempo * 3600)

# horas
horas = int(tempo_s / 3600)

# parte inteira restante
tempo_s = int(tempo_s % 3600)

# minutos
minutos = int(tempo_s / 60)

# o resto
segundos = int(tempo_s % 60)

# imprimir o tempo em horas, minutos e segundos
print("%05d:%02d:%02d" % (horas, minutos, segundos))