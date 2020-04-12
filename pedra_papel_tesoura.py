#Importo a biblioteca para escolha aleatória
from random import randint

#Crio a lista com os nomes dos itens que o computador pode escolher
itens = ('Pedra', 'Papel', 'Tesoura')

#Peço para o computador escolher um número aleatório dentro da lista
computador = randint(0,2)

#Digo ao jogador quais as suas opções:
print('''Selecione a sua opção: 
	[0] para Pedra
	[1] para Papel
	[2] para Tesoura
	''')

#Pergunto ao jogador qual a opção dele
escolhajogador = int(input('Qual a sua opção?'))

#Insiro as mensagens do que cada um escolheu
print('-='*15)
print("Você escolheu {}".format(itens[escolhajogador]))
print("O computador escolheu {}".format(itens[computador]))
print('-='*15)

#Crio as condições e mostro o resultado de cada uma
if computador == 0:
    if escolhajogador == 0:
        print('Empatou!')
    elif escolhajogador == 1:
        print('Você ganhou!')
    elif escolhajogador == 2:
        print('Você Perdeu!')
    else: print('Jogada inválida!')

if computador == 1:
    if escolhajogador == 0:
        print('Você Perdeu!')
    elif escolhajogador == 1:
        print('Empatou!')
    elif escolhajogador == 2:
        print('Você Ganhou!')
    else: print('Jogada inválida!')
if computador == 2:
    if escolhajogador == 0:
        print('Você Ganhou!')
    elif escolhajogador == 1:
        print('Você Perdeu!')
    elif escolhajogador == 2:
        print('Empatou!')
    else: print('Jogada inválida!')
