cpf = str(input('Digite seu CPF: '))
cont = 10
x = 0
resultado = 0
#checar se todos os algarismos são iguais
checker_1 = cpf[0]
checker_1 = int(cpf[0])
equal_numbers = 0
for i in range(11):
    checker_2 = int(cpf[x])
    if checker_2 == checker_1:
        equal_numbers+=1
    x+=1
if equal_numbers == 11:
    print('CPF INVÁLIDO, TODOS OS NÚMEROS SÃO IGUAIS')
else:
    x = 0
    for c in range(9):
        algarismo = int(cpf[x])
        x+=1
        calculador = algarismo * cont
        cont-=1
        resultado+=calculador
    a = (resultado * 10) % 11
    if a == 10:
        a = 0
    if a == int(cpf[9]):
        cont = 11
        x = 0
        resultado = 0
        for c in range(10):
            algarismo = int(cpf[x])
            x+=1
            calculador = algarismo * cont
            cont-=1
            resultado+=calculador
    b = (resultado * 10) % 11
    if b == 10:
        b = 0
    if a == int(cpf[9]) and b == int(cpf[10]):
        print("CPF APROVADO")
    else:
        print('CPF INVÁLIDO')

