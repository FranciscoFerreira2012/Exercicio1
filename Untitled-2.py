ordenado = float(input("Qual é o seu ordenado atual?"))
if ordenado < 500:
   reajuste = 15
   print("O seu ordenado reajustado é de", ordenado*reajuste/100)
elif ordenado <= 1000:
   reajuste = 10
   print("O seu ordenado reajustado é de", ordenado*reajuste/100)
else:
   reajuste = 5
   print("O seu ordenado reajustado é de", ordenado*reajuste/100)
