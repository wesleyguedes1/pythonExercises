numero = int(input('Digite um número: '))
potencia = int(input('Digite a potência: '))
resultado = 0
for c in range(1, numero+1):
    resultado+= c ** potencia
print("A soma de 1 até ", numero, "na potência", potencia, 'é igual a ', resultado)
