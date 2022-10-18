# Escreva um programa que pergunte a quantidade de Km percorridas por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$6 por dia e R$0.15 por Km rodado.
print('Calculador de Aluguel de Veiculos\n') # Mostra para o usuario o que o programa faz
k = float(input('Coloque os KMs Rodados: ')) # Variavel em tipo float para usuario colocar os kms rodados com o carro.
d = float(input('Coloque Quantos dias o Veiculo Foi Alugado: ')) # Variavel em tipo float para usuario colocar os dias que o veiculo foi alugado.
totalk = float(k * 0.15) # Variavel totalk em tipo float, pegando o valor inserido na variavel 'k' e multiplicando por 0.15.
totald = float(d * 60) # Variavel totald em  tipo float, pegando o valor inserido na variavel 'd' e multiplicando por 60.
total = totald + totalk # Variavel total que soma o resultado das duas variaveis (totald e totalk)
print('Total a Pagar pelos dias alocados R$ {:.2f} \n' # Mostra para o usuario o total a pagar pelos dias alugados.
      'O total a pagar por Kilometragem R$ {:.2f} \n' # Mostra para o usuario o total a pagar pelos Kms rodados.
      'Total do aluguel R$ {:.2f}'.format(totald, totalk, total)) # Mostra o total do aluguel do veiculo.
