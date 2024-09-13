"""Cabeçalho 015:
Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado."""

kmRodado = float(input('Quantos km´s o carro andou? '))
diasAlugado = int(input('Quantos dias o carro ficou alugado? '))
valorKmRodado = kmRodado * 0.15
valorDiasAlugado = diasAlugado * 60
print(f'O carro foi alugado durante {diasAlugado} dias e percorreu uma distância de {kmRodado}km rodados no total.')
print(f'O total a pagar é: R${valorDiasAlugado} pelos dias alugados.\nE R${valorKmRodado} pelos {kmRodado}km rodados.')
print(f'O total a ser pago é de: R${valorKmRodado+valorDiasAlugado}')