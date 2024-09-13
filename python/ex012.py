"""Cabeçalho 012:
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto."""

preco = float(input('Qual é o preço do produto? '))
desconto = int(input('Qual é a % de desconto? '))
novoPreco = preco - (preco * desconto / 100)
print(f'O produto que custava R${preco}, na promoção com desconto de {desconto}%, vai custar R${novoPreco:.2f}')

#----------------------------------------------------------------------------------------------------------------------------------

"""precoProduto = float(input('Qual o preço do produto? R$'))
porcentagemPromocao = float(input('Qual a porcentagem de desconto? '))
novoPreco = precoProduto * porcentagemPromocao / 100
print(f'O produto que custava: R${precoProduto}, na promoção com desconto de {porcentagemPromocao}%, vai custar R${novoPreco}.')"""