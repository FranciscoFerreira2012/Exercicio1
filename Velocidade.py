velocidade = int(input("Qual é a sua velocidade?"))
if velocidade>80:
    velocidadeExcesso = (velocidade-80)*2
    print("Estás acima do limite permitido. A multa foi gerada no valor de {} euros".format(velocidadeExcesso))
else:
    print("Dentro do limite. Boa viagem!")