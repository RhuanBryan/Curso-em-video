"""Cabeçalho 008:
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A distância de {medida}m corresponde a: \nKM: {km} \nHM: {hm} \nDAM: {dam} \nDM: {dm} \nCM: {cm} \nMM: {mm} \n')