"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#FEITO COM TRY E EXCEPET PARA VERIFICAR OS DADOS
num_1 = input('Digite um número: ') 
try:
    num_1_int = int(num_1)
    par_impar = num_1_int % 2 == 0
    if par_impar:
        print('Número par')
    else:
        print('numero impar')
except:
    print('Valor incorreto!')

#FEITO COM O ISDIGIT PARA VERIFICAR SE ERA NÚMERO INTEIRO
# num_1 = input('Digite um número: ')
# if num_1.isdigit():
#     num_1_int = int(num_1)
#     par_impar = num_1_int % 2 == 0
#     if par_impar:
#         print('Número par')
#     else:
#         print('numero impar')
# else:
#     print('Valor incorreto!')

#FEITO COM VERFICAÇÃO MANUAL E DE FORMA MAIS LONGA O ALGORITMO
# num_1 = input('Digite um número: ')
# num_1_int = int(num_1)
# if num_1_int % 2 == 0 and num_1_int:
#     print('Número par')
# elif num_1_int == False:
#     print('Valor incorreto')
# else:
#     print('numero impar')
