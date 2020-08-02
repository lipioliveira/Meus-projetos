#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
num = float(input("Insira o número que você gostaria de ver a parte inteira:"))
from math import trunc

print("O valor digitado é {} e sua parte inteira é {}".format(num,trunc(num)))