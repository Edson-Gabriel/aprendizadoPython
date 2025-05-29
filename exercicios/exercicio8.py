frase = '''Gabriel é lindo
e muito cheiroso'''
i = 0
qtd_maior = 0
letra_mais_vezes =''
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == ' ':
        i+=1
        continue
    qtd_atual = frase.count(letra_atual)
    if qtd_maior < qtd_atual:
        qtd_maior = qtd_atual
        letra_mais_vezes = letra_atual
    i += 1

print(
    'A letra que apareceu mais vezes na frase: '
    f'{frase} foi '
    f'"{letra_mais_vezes}" que apareceu '
    f'{qtd_maior}X'
)