import random
valor_dados= str(input('Digite a quantidade de dados e o número de faces do dado (por exemplo "1d20"): '))
x = list(valor_dados.split('d'))
print(x)
contador = int(x[0])
faces_dado = int(x[1])
resultados = list()
for c in range(contador):
    rolagem = random.randint(1, faces_dado)
    resultados.append(rolagem)
print(resultados)