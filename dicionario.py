ListaClientes = list()
CadastroClientes = dict()
for c in range (3):
    CadastroClientes['nome'] = str(input('Digite seu nome: '))
    CadastroClientes['idade'] = int(input('Digite sua idade: '))
    CadastroClientes['sexo'] = str(input('Digite seu sexo (M/F): '))
    ListaClientes.append(CadastroClientes.copy())
print(ListaClientes)
cont = 0
for r in ListaClientes:
    print(ListaClientes[cont]['nome'])
    cont+=1