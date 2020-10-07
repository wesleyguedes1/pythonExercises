real = float(input('Digite um valor em R$: '))
dolar = real / 5.02
euro = real / 5.36
print('O valor de R$ {} corresponde à: '.format(real))
print('{:.2f} USD'.format(dolar))
print('{:.2f} EUR'.format(euro))