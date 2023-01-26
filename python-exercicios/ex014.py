qkm = int(input('Quantos km rodados? Km'))
qdia = int(input('Quantos dias foi alugado? Dias'))
pago = (qdia * 60) + (qkm * 0.15)

print()

print('O total a pagar é {:.2f}'.format(pago))
