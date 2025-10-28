ordenado = float(input("Qual é o seu ordenado atual?"))
if ordenado < 500:
   reajuste = 15
elif ordenado <= 1000:
   reajuste = 10
else:
   reajuste = 5
ordenadoAumento = (ordenado*reajuste)/100
ordenadoFinal = ordenado + ordenadoAumento

print(f"O seu ordenado reajustado é de{ordenadoFinal}")
