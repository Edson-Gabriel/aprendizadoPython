"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#FOI FEITO COM O PROFESSOR A VALIDAÇÃO DOS DADOS
hora = input('São que horas? ')
try:
    hora_int = float(hora)
    dia = hora_int<=11 or hora_int == 24
    tarde = hora_int <= 17
    noite = hora_int <= 23

    if dia:
        print('Bom dia')
    elif tarde:
        print('Boa tarde')
    elif noite:
        print('Boa noite')
    else:
        print('Horário incorreto')
except:
    print('VALORES INCORRETOS')


#SOLUÇÃO ENCONTRADA SOZINHO
# hora = input('São que horas? ')
# if hora.isdigit():
#     hora_int = float(hora)
#     dia = hora_int<=11 or hora_int == 24
#     tarde = hora_int <= 17
#     noite = hora_int <= 23

#     if dia:
#         print('Bom dia')
#     elif tarde:
#         print('Boa tarde')
#     elif noite:
#         print('Boa noite')
#     else:
#         print('Horário incorreto')
# else:
#     print('VALORES INCORRETOS')