"""Qual é o volume de uma esfera com raio 5?"""
import math
raio = 5
volume = 4/3 * math.pi * math.pow(float(raio),3)
print(volume)

"""Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias"""
livro = 24.95
livroDesc = 24.95 * 40 / 100
copias = 60 * livroDesc
transporte_um = 3
exemplar_adicional = 59 * 0.75
totalAtacado = copias + transporte_um + exemplar_adicional
print(totalAtacado)
"""Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?"""
from datetime import timedelta

sairCasa = timedelta(hours=6, minutes=52, seconds=0)
km = timedelta(hours=0, minutes=8, seconds=15)
km3 = timedelta(hours=0, minutes=7, seconds=12)
km1 = timedelta(hours=0, minutes=8, seconds=15)

print(km + km3 + km1)