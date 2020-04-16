valornacarteira = float(input('Quantos reais você tem na carteira? R$'))

##Dólar em 15/04/2020 está 5,24
print('Com o valor de R${:.2f} você pode comprar ${:.2f} dólares'.format(valornacarteira, (valornacarteira/5.24)))