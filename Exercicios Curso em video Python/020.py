#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos 
# dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
nome1 = str(input("Insira o primeiro nome:"))
nome2 = str(input("Insira o segundo nome:"))
nome3 = str(input("Insira o terceiro nome:"))
nome4 = str(input("Insira o quarto nome:"))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print("A ordem escolhida aleatoriamente será: {}".format(lista))