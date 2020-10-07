n = int(input('Digite um número: '))
binario = list()
while True:
    resto = n % 2
    quociente = n // 2
    binario.append(resto)
    n = quociente
    if quociente == 0:
        break
x = list(reversed(binario))
print(x)