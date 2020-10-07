listaPessoas = []
lista_mulheres = []
soma_idade = 0
cadastroPessoas = dict()
for r in range (3):
    cadastroPessoas['nome'] = str(input('Digite seu nome: '))
    cadastroPessoas['sexo'] = str(input('Sexo(M/F): '))
    if cadastroPessoas['sexo'] == 'F' or cadastroPessoas['sexo'] == 'f':
        lista_mulheres.append(cadastroPessoas['nome'])
    cadastroPessoas['idade'] = int(input('Digite sua idade: '))
    soma_idade+= cadastroPessoas['idade']
    listaPessoas.append(cadastroPessoas.copy())
media_idade = soma_idade/len(listaPessoas)
idade_acima_media = []
cont = 0
for r in listaPessoas:
    if cadastroPessoas['idade'] > media_idade:
        idade_acima_media.append(cadastroPessoas['nome'])
print(listaPessoas)
print(media_idade)
print(lista_mulheres)
print(idade_acima_media)
