cadastro = dict()
cadastro['nome'] = str(input('Digite seu nome: '))
cadastro['data_nascimento'] = int(input('Digite o ano de seu nascimento: '))
cadastro['carteira_trabalho'] = int(input('Digite sua carteira de trabalho: '))
cadastro['ano_contrato'] = int(input('Digite o seu ano de contratação: '))
cadastro['salario'] = int(input('Digite seu salário: '))
cadastro['idade'] = 2020 - cadastro['data_nascimento']
cadastro['idade_aposentadoria'] = ((cadastro['ano_contrato'] + 35)-2020)+ cadastro['idade']
