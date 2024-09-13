from math import sin, cos, tan, radians

angulo = int(input('Qual é o ângulo? '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print(f'O ângulo é de {angulo}°, então o valor do(a): \nSeno é {sen:.2f}° \nCosseno é {cos:.2f}° \nTangente é {tan:.2f}°')
