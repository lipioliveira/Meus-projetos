custoAluguelPorDia = 60
custoPorKmRodado = 0.15
quantidadeDeDias = int(input("Quantos dias você ficou com o carro?"))
quantidadeDeKmRodados = int(input("Quantos km você andou?"))
custoTotal = (quantidadeDeDias * custoAluguelPorDia)+ (quantidadeDeKmRodados*custoPorKmRodado)
print("O custo total do aluguel é de R${:.2f}".format(custoTotal) )