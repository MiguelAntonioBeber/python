import random

a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do quarto aluno: '))
a5 = str(input('Nome do quinto aluno: '))

lista = [a1, a2, a3, a4, a5]

print()

e = random.choice(lista)
print('O aluno escolhido é {}'.format(e))