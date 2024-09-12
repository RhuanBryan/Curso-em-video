kmRodado = float(input('Quantos km´s o carro andou? '))
diasAlugado = int(input('Quantos dias o carro ficou alugado? '))
valorKmRodado = kmRodado * 0.15
valorDiasAlugado = diasAlugado * 60
print(f'O carro foi alugado durante {diasAlugado} dias e percorreu uma distância de {kmRodado}km rodados no total.')
print(f'O total a pagar é: R${valorDiasAlugado} pelos dias alugados.\nE R${valorKmRodado} pelos {kmRodado}km rodados.')
print(f'O total a ser pago é de: R${valorKmRodado+valorDiasAlugado}')