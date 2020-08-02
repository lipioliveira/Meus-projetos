#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.#
from math import hypot
catetoOposto = float(input("Qual o tamanho do cateto oposto?"))
catetoAdjacente = float(input("Qua o tamanho do cateto adjacente?"))
hipotenusa = hypot(catetoOposto,catetoAdjacente)

print("O valor da hipotenusa é {:.0f}".format(hipotenusa))