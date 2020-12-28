# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Sem Biblioteca
number = float(input('Digite Um Numero Real: ')) # Varialvel number responsavel por guardar o numero real inserido pelo usuario.
number1 = round(number) # Variavel number1 contendo uma função chamada 'round' onde recebe dois parametros e arredonda com uma porção inteira.
print('O numero {} tem a parte Inteira {}'.format(number, number1)) # Mostra para o usuario o numero inserido e a parte inteira dela.
