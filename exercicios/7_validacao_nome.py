"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#NESSE FIZ A VALIDAÇÃO DE LETRAS MINIMAS NO NOME COM O PROFESSOR (NÃO É DIFICIL, PORÉM NÃO TINHA PENSADO EM FAZER ESSE VALIDADOR)
name = input('Digite seu primeiro nome: ')
if len(name) > 1:
    name_short = len(name) <= 4
    name_normal = len(name) <= 6
    name_big = len(name) > 6

    if name_short:
        print('Seu nome é curto')
    elif name_normal:
        print('Seu nome é normal')
    elif name_big:
        print('Seu nome é grande')
    else:
        print('DADOS INCORRETOS')   
else:
    print('Digite mais de uma letra')


#SOLUÇÃO ENCONTRADA SOZINHO
# name = input('Digite seu primeiro nome: ')
# name_short = len(name) <= 4
# name_normal = len(name) <= 6
# name_big = len(name) > 6

# if name_short:
#     print('Seu nome é curto')
# elif name_normal:
#     print('Seu nome é normal')
# elif name_big:
#     print('Seu nome é grande')
# else:
#     print('DADOS INCORRETOS')   