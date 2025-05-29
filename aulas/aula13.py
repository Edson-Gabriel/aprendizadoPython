#Aqui entramos no mundo das formatações de string
#Precisei da ajuda do professor, pos não lembrava
#como que usava as "f str"
nome = 'Gabriel'
altura = 1.73
peso = 72
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Luiz Otávio tem 1.80 de altura,
# pesa 95 quilos e seu IMC é
# 29.320987654320987