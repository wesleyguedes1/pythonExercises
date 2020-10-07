from random import randint
numeros = []
n_pares = 0
def sorteia():
    for c in range (10):
        x = randint(0, 100)
        numeros.append(x)
def soma_par():
    global n_pares
    for n in numeros:
        if n%2 ==0:
            n_pares+=n
sorteia()
soma_par()
print('Os números sorteados foram', numeros)
print('A soma dos números pares desta lista é igual à', n_pares)
