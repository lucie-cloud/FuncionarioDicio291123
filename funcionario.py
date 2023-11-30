# Cadastro de funcionários

# Estrutura dicionário

funcionário = {'Nome': '', 'Salário': 0.0, 'Ativo': False}


# Entradas
print('\n\t\t\t -- Registro de Funcionário -- \n')

funcionário ['Nome'] = input('Informe o nome: ')
funcionário ['Salário'] = float(input('Informe o salário: R$ '))
funcionário ['Ativo'] = True

# Saída
print(f'\n\n Nome.....{funcionário["Nome"]}')
print(f'Salário........{funcionário["Salário"]}')
print("*** Funcionário Ativo ***") if funcionário ['Ativo'] else print("*** Funcionário Inativo *** ")