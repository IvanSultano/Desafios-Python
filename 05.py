print('Conversor de Moedas\n') # Printa para o usuario a mensagem
number = float(input('Digite quantos Reais Você Possue:')) # A variavel number tipo float feita para o usuario colocar sua quantidade de reias que deseja converter
conversion = number / 3.27 # Variavel conversion pega o valor que o usuario inseriu e divide por 3.27
print('Você Possui {:.2f} Dolares'.format(conversion)) # Printa para o usuario a conversão da quantidade em Reias para Dolares
