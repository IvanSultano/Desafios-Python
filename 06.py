# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
width = float(input('Largura Da Parede: ')) # A variavel width guarda a largura da parede digitada pelo usuario em tipo float
height = float(input('Digite a Altura da Parede: ')) # A variavel height guarda a altura da parede digitada pelo usuario em tipo float
area = width * height # Criada uma variavel area para fazer a operação de largura vezes a altura da parede que foi digitada pelo usuario nas variaveis width e height
liters = area / 2 # Criada para calcular quantos litros de tinta o usuario vai precisar para pintar a area colocada, operação dividindo a area por 2
print('Você vai precisar de {} Para Pintar sua area'.format(liters)) # Printa para o usuario quantos litros de tinta irá precisar para pintar a area 