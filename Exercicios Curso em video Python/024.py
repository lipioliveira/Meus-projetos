#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
nomeRecebido = str(input("Insira seu nome:")).strip()
print(nomeRecebido[:5].lower() == "santo")