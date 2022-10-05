"""Quantos segundos há em 42 minutos e 42 segundos?"""
minutos = 42
segundos = 42
conversao = (minutos * 60) + segundos
print(conversao)

"""Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro."""
milhas = 1.61
km = 10
milhasTotal = milhas * km
print(milhasTotal)

"""Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?"""
horas  = conversao / 3600
velocidadeMedia = milhasTotal / horas
print(velocidadeMedia)