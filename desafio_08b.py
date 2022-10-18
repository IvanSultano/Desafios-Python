# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Com Biblioteca
import math
num = float(input('DIgite um valor real: '))
print('O numnero {} tem a parte Inteira {}'.format(num, math.trunc(num)))
