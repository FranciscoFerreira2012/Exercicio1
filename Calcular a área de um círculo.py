from math import pi

def CalculoDaÁrea ():
    RaioDoCirculo = float(input('Qual é o comprimento do raio em centímetros?'))
    AreaDoCirculo = pi*(RaioDoCirculo**2)
    print(f'A área do círculo é de {AreaDoCirculo} centímetros')

CalculoDaÁrea ()