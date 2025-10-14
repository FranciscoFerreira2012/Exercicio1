y = int(input("Quantos euros deseja converter?\n"))
print("Qual moeda deseja converter:\n[0] Real Brasileiro\n[1] Bath Tailandês")
x = input("Escolha sua opção")
if x ==0:
    y*6.34
    print("Isso lhe dará", y)
else:
    y*37.91
    print("Isso lhe dará", y)