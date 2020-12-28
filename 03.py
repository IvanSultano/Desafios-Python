number1 = float(input('Digite a Primeira Nota: ')) # O usuario digita a primeira nota do aluno em tipo float
number2 = float(input('Digite a Segunda Nota: ')) # O usuario digita a segunda nota  do aluno em tipo float
sum = (number1 + number2) / 2 # Variavel sum faz a soma das duas notas que o usuario incluiu em seguida fazendo essa soma dividido por 2
print('As notas Digitadas Foram {}, {}\n' # Printa para o usuario as notas que o usuario incluiu 
      'A Media Do aluno é {}'.format(number1, number2, sum)) # Printa a variavel sum com a media das notas
