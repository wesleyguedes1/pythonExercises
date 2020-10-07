n = int(input("Digite um número: "))
q = str(input("Deseja continuar?(s/n)"))
soma = n
quant = 1
menor = n
media = 0
maior = n
while q== "s":
    n = int(input("Digite um número:"))
    q = str(input("Deseja continuar?(s/n)"))
    quant+=1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma+=n
    media = soma/quant
print("Você digitou", quant, "números. O maior deles foi", maior, "e o menor foi", menor)
print("A média desses números é igual a", media)

