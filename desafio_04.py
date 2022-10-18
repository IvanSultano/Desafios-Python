# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
print('Conversor de Metros Para Centimetros\n') # Printa para o usuario a mensagem
number = float(input('Insira os Metros que Deseja converter: ' )) # Variavel tipo float para o usuario digitar os metros que pretende converter para centimetros
conversion = number * 100 # variavel conversion faz a operação dos metros digitados vezes 100
print('Os metros inseridos são {}\n' # Mostra os metros que o usuario inseriu 
      'A conversão em centimetros são {}'.format(number, conversion)) # Mostra para o usuario a solução da variavel conversion de metros para centimetros
