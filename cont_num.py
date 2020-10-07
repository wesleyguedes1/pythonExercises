quant = 0
soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    quant+=1
    soma+=n
print("Você digitou", quant, "números, e a soma deles é igual a", soma)
