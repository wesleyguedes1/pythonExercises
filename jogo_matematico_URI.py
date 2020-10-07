char = str(input('Digite os caracteres: '))
letra = char[1]
if char[0] == char[2]:
    resultado = int(char[0]) * int(char[2])
    print(resultado)
elif letra.isupper() == True:
    resultado = int(char[2]) - int(char[0])
    print(resultado)
elif letra.islower() == True:
    resultado = int(char[0]) + int(char[2])
    print(resultado)