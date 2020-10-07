n = list(reversed(str(input('Digite o número em binário: '))))
n_lenght = int(len(n))
exp = int(0)
resultado = 0
while exp < n_lenght:
    algarismo = int(n[exp])
    equacao = (algarismo*2) ** exp
    if n[0] == '0' and exp == 0:
        equacao = 0
    exp+=1
    resultado+= equacao
print(resultado)
