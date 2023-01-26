from math import radians, sin, cos, tan

an = float(input('Digite o ângulo que você deseja: '))

print()

seno = sin(radians(an))
print('O ângulo de {} tem o SENO {:.2f}'.format(an, seno))

print()

cosseno = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))

print()

tangente = tan(radians(an))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(an, tangente))