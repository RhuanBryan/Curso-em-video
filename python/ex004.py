a = input('Digite algo: ')

caracteristicas = []

if a.isspace():
    caracteristicas.append('contém apenas espaços')
elif a.isnumeric():
    caracteristicas.append('é numérico')
elif a.isalpha():
    caracteristicas.append('é alfabético (só contém letras)')
elif a.isalnum():
    caracteristicas.append('é alfanumérico (contém letras e números)')

if a.isupper():
    caracteristicas.append('está em maiúsculas')
elif a.islower():
    caracteristicas.append('está em minúsculas')
elif a.istitle():
    caracteristicas.append('está capitalizado (primeira letra maiúscula e o restante minúsculo)')

if caracteristicas:
    print(f'O valor "{a}" ' + ' e '.join(caracteristicas) + '.')
else:
    print(f'O valor "{a}" não se encaixa em nenhuma das características listadas.')

#---------------------------------------------------------------------------------------------------------

"""print('O tipo primitivo desse valor é: ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está captalizada? ', a.istitle())
if a == a.isnumeric():
    print(a, ' é numérico!')
else:
    print('Não sei o que {} é!'.format(a))"""

#---------------------------------------------------------------------------------------------------------

"""if a.isnumeric():
    print(a, 'é numérico!')
else:
    print('Não sei o que {} é!'.format(a))"""

#---------------------------------------------------------------------------------------------------------

"""if a.isspace():
    print(f'O valor "{a}" contém apenas espaços.')
elif a.isnumeric():
    print(f'O valor "{a}" é numérico.')
elif a.isalpha():
    print(f'O valor "{a}" é alfabético (só contém letras).')
elif a.isalnum():
    print(f'O valor "{a}" é alfanumérico (contém letras e números).')

if a.isupper():
    print(f'O valor "{a}" está em maiúsculas.')
elif a.islower():
    print(f'O valor "{a}" está em minúsculas.')
elif a.istitle():
    print(f'O valor "{a}" está capitalizado (primeira letra maiúscula e o restante minúsculo).')
else:
    print(f'O valor "{a}" tem uma mistura de maiúsculas e minúsculas ou outros caracteres.')"""

#---------------------------------------------------------------------------------------------------------