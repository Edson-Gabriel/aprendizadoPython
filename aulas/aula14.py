#Aula de formatação de str com o método .format
a = 'AAAAA' #Aqui são valores que deixamos na váriavel
b = 'BBBBBB' #Aqui são valores que deixamos na váriavel
c = 1.1 #Aqui são valores que deixamos na váriavel
string1 = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}' #Aqui vamos atribuir um método para cada chave
formato1 = string1.format(
    nome1=a, nome2=b, nome3=c
) #Aqui ta o pulo do gato. Chamamos o meodo .format e nela atribuimos posições nomeais. Ex: Var "a" tem o "nome1" então toda vez que chamar ela sou obrigado a chamar ela por esse nome
print(formato1)
d = 'DDDDDD' #Aqui são valores que deixamos na váriavel
e = 'EEEEEE' #Aqui são valores que deixamos na váriavel
f = 2.1 #Aqui são valores que deixamos na váriavel
string2 = 'd={0} e={1} e={2} f={2:.2f}' #Aqui vamos atribuir um método para cada chave
formato2 = string2.format(d, e, f) #Diferente de antes q usamos por nome, aqui usamos por indice. Então sou obrigado a chamar no método o indice correto de cada uma das "funções que fiz"
print(formato2)