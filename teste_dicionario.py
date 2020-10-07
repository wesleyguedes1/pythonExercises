import random
listaNumeros = list()
for r in range (10):
    listaNumeros.append(random.randint(0, 20))
alvo = int(input('Digite o número à ser procurado na lista: '))
min = 0
max = (len(listaNumeros)) -1
chute = (min + max)//2
while True:
    
    if listaNumeros[chute] < alvo:
        min = chute + 1
    if listaNumeros[chute] > alvo:
        max = chute - 1
    if listaNumeros[chute] == alvo:
        print('O alvo está na lista!')
        break
    if max < min :
        print('O número alvo não está na lista.')
        break
    chute = (min + max)//2
print(listaNumeros)



