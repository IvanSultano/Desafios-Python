print('Calculador de Aluguel de Veiculos\n')
k = float(input('Coloque os KMs Rodados: '))
d = float(input('Coloque Quantos dias o Veiculo Foi Alugado: '))
totalk = float(k * 0.15)
totald = float(d * 60)
total = totald + totalk
print('Total a Pagar pelos dias alocados R$ {:.2f} \n'
      'O total a pagar por Kilometragem R$ {:.2f} \n'
      'Total do aluguel R$ {:.2f}'.format(totald, totalk, total))
