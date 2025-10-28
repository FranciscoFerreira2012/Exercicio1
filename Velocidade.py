velocidade = int(input("Qual é a sua velocidade?"))
if velocidade>120:
    velocidadeExcesso = (velocidade-120)*4
    print("Estás muito acima do limite permitido. A multa foi gerada no valor de {} euros".format(velocidadeExcesso))
elif velocidade>80:
    velocidadeExcesso = (velocidade-80)*2
    print("Estás acima do limite permitido. A multa foi gerada no valor de {} euros".format(velocidadeExcesso))
else:
    print("Está detro do limite. Boa viagem!")
    
