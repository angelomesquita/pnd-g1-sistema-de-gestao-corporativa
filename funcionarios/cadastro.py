# módulo de cadastro de funcionarios
# funcionarios/cadastro.py

funcionarios = []

def cadastrar_funcionario():
    nome = input("Digite o nome do funcionário: ")
    cargo = input("Digite o cargo do funcionario: ")
    salario = float(input("Digite o salário do funcionario: "))
    
    funcionario = {"nome": nome, "cargo": cargo, "salario": salario}
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso.")
