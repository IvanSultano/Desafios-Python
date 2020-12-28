# Faça um programa que Leia um numero em tipo Inteiro e mostre o valor dele em dobro e o triplo.
number = int(input('Digite um Numero: ')) #O usuario digita um numero em tipo inteiro
double = number * 2 # A variavel double faz a operação number vezes 2
triple = number * 3 # A variavel triple faz a operaçãonumber vezes 3
print('O Numero digitado foi {}\n' # Mostra para o usuario qual numero ele digitou 
      'O seu Numero em Dobro é {}\n' # Mostra a variavel double (O dobro do numero digitado pelo usuario)
      'O seu Numero Triplicado é {}'.format(number, double, triple)) # Mostra a variavel triple (O tripo do numero digitado pelo usuario)
