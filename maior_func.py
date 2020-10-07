maior = 0
quant = 0
def maior_cont():
    global maior
    global quant
    while True:
        n = int(input('Digite um número: '))
        if n < 0:
            break
        if n > maior:
            maior = n
        quant+= 1
    print(quant, 'números foram digitados, sendo', maior , 'o maior deles.')
maior_cont()
        
