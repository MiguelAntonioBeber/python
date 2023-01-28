import random

aluno1 = str(input('Nomo do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceiro aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
aluno5 = str(input('Nome do quinto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4, aluno5]

random.shuffle(lista)

print()

print('A ordem dos alunos é: {}'.format(lista))

