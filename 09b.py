''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa. Com Biblioteca '''

import math
oppositeside = float(input('Digite o valor do cateto oposto: '))
adjacentside = float(input('Digite o valor do cateto adjacente: '))
hypotenuse = math.hypot(oppositeside, adjacentside)
print('O comprimento da hipotenusa é: {:.2f}'.format(hypotenuse))
