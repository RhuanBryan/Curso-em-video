n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
s = n1 + n2
m = s / 2
#m = (n1 + n2) / 2
print(f'A soma entre as duas notas do aluno é: {s:.1f}.\nA média do aluno é: {m:.1f}')
if m > 6:
    print('O aluno foi aprovado!')
else:
    print('O aluno foi reprovado!')
