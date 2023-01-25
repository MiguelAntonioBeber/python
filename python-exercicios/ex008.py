distancia = float(input('Digite uma distancia em metros: '))

km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000

print('A medida {:.0f} corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(distancia, km, hm, dam, dm, cm, mm))
