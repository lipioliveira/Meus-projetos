#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
primeiroNome = str(input("Insira o primeiro nome:"))
segundoNome = str(input("Insira o segundo nome:"))
terceiroNome = str(input("Insira o terceiro nome:"))
quartoNome = str(input("Insira o quarto nome:"))
lista = [primeiroNome, segundoNome, terceiroNome, quartoNome]

print("O nome escolhido foi o do {}".format(choice(lista)))