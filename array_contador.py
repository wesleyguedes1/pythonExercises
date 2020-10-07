x = []
soma = 0
maior = 0
while True:
    n = int(input('Digite um número: '))
    if n == 0:
        break
    x.append(n)
print(x)
for c in x:
    soma+=c
    if c > maior:
        maior = c
quant = len(x)
media = soma/quant
print("A média dos números é igual à", media)
print("A soma dos números é igual à", soma)
print("O maior número é", maior)