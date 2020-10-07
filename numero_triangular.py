n = int(input('Digite um número: '))
for c in range(1, n+1):
    if c * (c+1) * (c+2) == n:
        print(n, 'é um número triangular.')
    else:
        print('não é um número triangular')