"""Calculadora científica: operações e interface de terminal."""
import math


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        raise ValueError('Divisão por zero não é permitida')
    return x / y


def potencia(x, y):
    return x ** y


def raiz_quadrada(x):
    if x < 0:
        raise ValueError('Raiz quadrada de número negativo não é real')
    return math.sqrt(x)


def fatorial(x):
    if isinstance(x, bool) or not isinstance(x, int) or x < 0:
        raise ValueError('Fatorial exige inteiro não negativo')
    return math.factorial(x)


def logaritmo_natural(x):
    if x <= 0:
        raise ValueError('Logaritmo exige número positivo')
    return math.log(x)


def logaritmo_base10(x):
    if x <= 0:
        raise ValueError('Logaritmo exige número positivo')
    return math.log10(x)


def seno(x):
    return math.sin(math.radians(x))


def cosseno(x):
    return math.cos(math.radians(x))


def tangente(x, radianos=False):
    angulo = x if radianos else math.radians(x)
    if math.isclose(math.cos(angulo), 0, abs_tol=1e-12):
        raise ValueError('Tangente indefinida para este ângulo')
    return math.tan(angulo)


def menu():
    print('Bem-vindo à Calculadora Científica')
    for indice, nome in enumerate(['Sair', 'Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Raiz Quadrada', 'Fatorial', 'Logaritmo Natural (ln)', 'Logaritmo Base 10', 'Seno', 'Cosseno', 'Tangente']):
        print(f'{indice}. {nome}')


def calculadora_cientifica():
    binarias = {'1': adicao, '2': subtracao, '3': multiplicacao, '4': divisao, '5': potencia}
    unarias = {'6': raiz_quadrada, '7': fatorial, '8': logaritmo_natural, '9': logaritmo_base10, '10': seno, '11': cosseno, '12': tangente}
    while True:
        menu()
        escolha = input('Digite o número da operação: ').strip()
        if escolha == '0':
            print('Calculadora encerrada.')
            return
        if escolha not in binarias and escolha not in unarias:
            print('Operação inválida. Tente novamente.')
            continue
        try:
            if escolha in binarias:
                x = float(input('Digite o primeiro número: '))
                y = float(input('Digite o segundo número: '))
                resultado = binarias[escolha](x, y)
            else:
                x = int(input('Digite o número: ')) if escolha == '7' else float(input('Digite o número ou ângulo em graus: '))
                resultado = unarias[escolha](x)
            print('Resultado:', resultado)
        except (ValueError, OverflowError, ZeroDivisionError) as erro:
            print('Erro:', erro)
        if input('Deseja realizar outra operação? (s/n): ').strip().lower() != 's':
            return


if __name__ == '__main__':
    calculadora_cientifica()
