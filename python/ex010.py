"""Cabeçalho 010:
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar."""

reais = float(input('Quantos R$ você tem? R$'))
dolar = 5.67
print(f'Com R${reais} você consegue comprar U${reais/dolar:.2f}')