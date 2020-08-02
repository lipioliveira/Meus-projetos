#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input("Digite o número:"))
unidade = num // 1 % 10
centena = num // 10 % 10
dezena = num // 100 % 10
milhar = num // 1000 % 10
print("A milhar é: {}".format(milhar))
print("A centena é: {}".format(centena))
print("A dezena é: {}".format(dezena))
print("A unidade é: {}".format(unidade))