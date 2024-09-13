"""Cabeçalho 013:
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento."""

salario = float(input('Qual é o salário do funcionário? R$'))
aumento = int(input('Qual a porcentagem de aumento no salário do funcionário? '))
novoSalario = salario + (salario * aumento / 100)
print(f'Seu salário aumentou {aumento}%. Agora você recebe R${novoSalario}')