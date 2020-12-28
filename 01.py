#Escreva um programa que o usuario digite um numero em tipo Inteiro e mostre o Antecessor e Sucessor.
number = int(input("Insira um Numero: "))  # Usuario Digita um numero em tipo inteiro
y = number - 1 # Programa pega o numero digitado pelo usuario e a variavel 'y' faz a operação 'number - 1'
x = number + 1 # Programa pega o numero digitado pelo usuario e a variavel 'x' faz a operação 'number + 1'
print('Numero Digitado Foi {}\n' # Ira printar para o usuario o numero que ele digitou
      'Antecessor do seu numero é {}\n' # Ira printar a variavel y, mostrando o numero digitado pelo usuario menos 1 ( Antecessor do numero digitado pelo usuario)
      'O sucessor é {}\n'.format(number, y, x)) # Ira printar a variavel x, mostrando o numero digitado pelo usuario mais 1 ( Sucessor do numero digitado pelo usuario)
