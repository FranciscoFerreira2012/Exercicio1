soma = 0
def contarletra():
    global soma
    frase = input('Digite a frase: ')
    letra = input('Que letra queres encontrar na frase? ')
    for x in frase:
        if letra in frase:
            soma += 1
    print(f'Nesta frase existem {soma} vezes a letra ({letra}) na sua frase.')       

contarletra()