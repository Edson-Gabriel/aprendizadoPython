while True:
    num1 = input('Digite o primeiro número: ')
    operador = input('Qual operação deseja (+-*/): ')
    num2 = input('Digite o segundo número: ')
    num1_float = 0
    num2_float = 0
    numeros_validos = None

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos números são inválidos.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue
    print('Segue abaixo o resultado da sua conta.')
    if operador == '+':
        print(num1_float + num2_float)
    elif operador =='-':
        print(num1_float - num2_float)
        # print(f'{num1_float}' - f'{num2_float}')
    elif operador == '*':
            print(num1_float * num2_float)
        # print(f'{num1_float}' * f'{num2_float}')
    elif operador == '/':
        print(num1_float / num2_float)
    else:
        print('Erro do cão')

    sair = input('Quer sair? (S para sim):').lower().startswith('s')
    if sair is True:
        break
