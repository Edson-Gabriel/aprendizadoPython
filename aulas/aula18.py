primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')
if primeiro_valor > segundo_valor:
    print(f'o {primeiro_valor=} é maior que o {segundo_valor=}')
elif primeiro_valor < segundo_valor:
    print(f'o {segundo_valor=} é maior que o {primeiro_valor=}')
else:
    print('Os valores são iguais')