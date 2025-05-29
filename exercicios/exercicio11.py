import os

lista_compra = []

while True:
    print('SELECIONE UMA OPÇÃO')
    opcao = input('(i)inserir (a)apagar (l)listar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compra.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        try:
            indice = int(indice_str) -1
            del lista_compra[indice]
        except:
            print('Não foi possível apagar esse indice')
    elif opcao =='l':
        os.system('cls')

        if len(lista_compra) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista_compra):
            print(i + 1, valor)
    else:
        print('Por favor, escolha i, a ou l.')