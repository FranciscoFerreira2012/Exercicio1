def Soma():
    return primeiroValor + segundoValor

def Subtração():
    return primeiroValor - segundoValor


def Divisão():
    return primeiroValor / segundoValor


def Multiplicação():
    return primeiroValor * segundoValor

def Cabecalho(texto):
    print()
    print('='*17)
    print(f'|| {texto} ||')
    print('='*17)
    print()

def Calculadora():
    global primeiroValor
    global segundoValor

    while True:
        Cabecalho('Calculadora')
        print(' 1 - Soma\n 2 - Subtrair\n 3 - Multiplicar\n 4 - Dividir\n 0 - Sair')
        print()
        escolha = int(input('Qual a sua escolha?'))
        print()
        if escolha == 0:
            break
        else:
            primeiroValor = float(input('Entre com o valor de A: '))
            segundoValor = float(input('Entre com o valor de B: '))
            if escolha == 1:
                resultado = Soma()
            elif escolha == 2:
                resultado = Subtração()
            elif escolha == 3:
                resultado = Multiplicação()
            elif escolha == 4:
                resultado = Divisão()
            print(f'\nO resultado da conta é {resultado:.2f}')
            input('\nEnter para Terminar')

Calculadora()