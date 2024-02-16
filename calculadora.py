import os

def calculadora():
    print('0 : Soma \n1 : Subtração \n2 : Multiplicação \n3 : Divisão \n4 : Exponenciação \n  \nEscolha a operação que deseja realizar:')
    operaçao = int(input())
    calculo(operaçao)

def calculo(operaçao):
    if operaçao == 0:
        x = 'soma'
    if operaçao == 1:
        x = 'subtração'
    if operaçao == 2:
        x = 'multipliação'
    if operaçao == 3:
        x = 'divisão'
    if operaçao == 4:
        x = 'exponenciaçao'
    print('>>>',x,'escolhida\n  \nQual o primeiro valor?')
    a = float(input())
    print('Qual o segundo valor?')
    b = float(input())
    if operaçao == 0:
        print()
        print('{} + {} = {}'.format(a, b, a+b),'\n  \n ================ \nDeseja fazer outra operação? 0 - SIM, 1 - NÃO')
        sn = int(input())
        if sn == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculadora()
    elif operaçao == 1:
        print()
        print('{} + {} = {}'.format(a, b, a+b),'\n  \n ================ \nDeseja fazer outra operação? 0 - SIM, 1 - NÃO')
        sn = int(input())
        if sn == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculadora()
    elif operaçao == 2:
        print()
        print('{} + {} = {}'.format(a, b, a+b),'\n  \n ================ \nDeseja fazer outra operação? 0 - SIM, 1 - NÃO')
        sn = int(input())
        if sn == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculadora()
    elif operaçao == 3:
        print()
        print('{} + {} = {}'.format(a, b, a+b),'\n  \n ================ \nDeseja fazer outra operação? 0 - SIM, 1 - NÃO')
        sn = int(input())
        if sn == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculadora()
    else:
        print()
        print('{} ** {} = {}'.format(a, b, a**b),'\n  \n ================ \nDeseja fazer outra operação? 0 - SIM, 1 - NÃO')
        sn = int(input())
        if sn == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            calculadora()

calculadora()
