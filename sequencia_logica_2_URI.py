X = int(input('Digite o primeiro algarismo: '))
Y = int(input('Digite o segundo algarismo: '))
c = 1
while c <= Y:
    if c % X == 0:
        print(c)
    else:
        print(c, ' ', end= ' ')
    c+=1