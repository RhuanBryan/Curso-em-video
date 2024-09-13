"""Cabeçalho 016:
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6."""

from math import floor, trunc

num = float(input('Digite um número para saber sua porção inteira: '))
print(f'A porção inteira do número digitado é {floor(num)}.')

#----------------------------------------------------------------------------

"""num = float(input('Digite um número para saber sua porção inteira: '))
print(f'A porção inteira do número digitado é {trunc(num)}.')"""

#----------------------------------------------------------------------------

"""num = float(input('Digite um número para saber sua porção inteira: '))
print(f'A porção inteira do número digitado é {int(num)}.')"""