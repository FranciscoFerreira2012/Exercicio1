ordenado = float(input("Qual é o seu ordenado atual?"))
x = (ordenado*reajuste/100)
if ordenado < 500:
   reajuste = 15
   print("O seu ordenado reajustado é de", x)
elif ordenado <= 1000:
   reajuste = 10
   print("O seu ordenado reajustado é de", x)
else:
   reajuste = 5
   print("O seu ordenado reajustado é de", x)
