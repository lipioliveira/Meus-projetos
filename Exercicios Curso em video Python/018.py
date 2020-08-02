from math import sin, cos, tan, radians
#Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
angulo = float(input("Qual o ângulo desejado?"))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print("O seno de {:.0f} é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.".format(angulo,seno, cosseno, tangente))