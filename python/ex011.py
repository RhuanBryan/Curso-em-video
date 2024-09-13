"""Cabeçalho 011:
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²."""

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
areaParede = altura * largura
lTinta = areaParede / 2
print(f'A área da parede é de {areaParede}m².\nVocê vai precisar de {lTinta}L de tinta para pintar a parede.')