#custo de viagem
#Programa para calcular o custo total de uma viagem

distancia = float(input("Qual é a distância da viagem em km?"))
print("\nEscolha o meio de transporte:")
print("1. Carro (0.50 euros por km)")
print("2. Comboio (0.30 euros por km)")
print("3. Avião (1.00 euros por km)")

meio_transporte = int(input("Digite o número correspondente ao meio de transporte: "))

if meio_transporte == 1:
    preço_por_km = 0.50
elif meio_transporte == 2:
    preço_por_km = 0.30
elif meio_transporte == 3:
    preço_por_km = 1.00
else:
    preço_por_km = 0
    print("Opção inválida. O custo não será calculado corretamente.")

quantidade_pessoas = int(input("\nInsira a quatidade de pessoas na viagem:"))

custo_total = distancia * preço_por_km * quantidade_pessoas

print("\nResumo de Viagem:")
print("Distância:" + str(distancia) + " km")
print("Preço por km: €" + str(preço_por_km))
print("Quantidade de pessoas:" + str(quantidade_pessoas))
print("Custo Total da Viagem: €" + str(custo_total))
