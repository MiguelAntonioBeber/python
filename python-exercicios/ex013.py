salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario * 15 / 100)

print()

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))

