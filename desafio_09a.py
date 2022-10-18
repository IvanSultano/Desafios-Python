''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa. Sem Biblioteca '''

oppositeside = float(input('Digite o valor do caeto oposto: '))
adjacentside = float(input('Digite o valor do cateto adjacente: '))
hypotenuse = (oppositeside ** 2 + adjacentside ** 2) ** (1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hypotenuse))

