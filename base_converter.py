base = int(input('Digite a base usada: '))
n = int(input('Digite um número: '))
resultado = list()
while True:
    resto = n % base
    quociente = n // base
    resultado.append(resto)
    n = quociente
    if quociente == 0:
        break
x = list(reversed(resultado))
print(x)