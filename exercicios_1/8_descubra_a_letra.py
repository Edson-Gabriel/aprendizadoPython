nome = input('Digite uma palavra, ou uma frase: ')
letra = input('Qual letra você quer descobrir: ')
indice = 0
while indice < len(nome):
    if nome[indice] == letra.lower() or nome[indice] == letra.upper():
        if nome[indice] == letra:
            print(f'{letra} no indice', indice + 1, f'{letra} minúsculo')
        else:
            print(f'{letra.upper()} no indice', indice + 1, f'{letra.upper()} maiúsculo')
    indice += 1
print(f'Acabou as letras {letra} na palavra {nome}')



# nome = 'Gabriel'
# tamanho = len(nome)
# print(tamanho)
# print(nome[:tamanho])
# tentativa =0
# while nome[:tentativa] != letra:
#     tentativa += 1
#     letra = nome[:tentativa]
#     print(letra)
    
# nome = 'Gabriel'
# tentativa = 0
# while tentativa < len(nome) and nome[tentativa] != letra:
#     tentativa += 1

# if tentativa < len(nome):
#     print(f"Letra letra encontrada na posição {tentativa}")
# else:
#     print("Letra letra não encontrada.")
