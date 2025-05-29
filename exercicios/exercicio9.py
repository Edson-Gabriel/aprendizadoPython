'''JOGO DE ADIVINHA A PALAVRA'''
import os

palavra_secreta = 'Gabriel'.upper()
letras_acertadas = ''
tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ').upper()
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite somente uma letra')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada+=letra_secreta
        else:
            palavra_formada+='*'

    print(f'PALAVRA FORMADA: {palavra_formada}')
    if palavra_formada == palavra_secreta:  
        os.system('cls')
        print(
            'VOCE GANHOU! PARABÉNS '
            f'A PALAVRA ERA {palavra_secreta} '
            f'PRECISOU DE {tentativas} CHANCES PARA ACERTAR')
        novo = input('QUER IR DE NOVO? [S/ PARA SIM] ').upper()
        if novo == 'S':
            letras_acertadas = ''
            tentativas = 0
            continue
        else:
            break    