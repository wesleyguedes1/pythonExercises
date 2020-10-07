# -*- coding: utf-8 -*-
n = int(input('Digite um número: '))
cont = n
fatorial = 1
for c in range(n):
    fatorial*= cont
    cont-= 1
print('O fatorial de', n, 'é', fatorial)