# módulo de cadastro de funcionarios
# funcionarios/cadastro.py

funcionarios = []

def cadastrar_funcionario(nome, cargo, salario):
    funcionario = {"nome": nome, "cargo": cargo, "salario": salario}
    funcionarios.append(funcionario)
    print(f"Funcionário {nome} cadastrado com sucesso.")
