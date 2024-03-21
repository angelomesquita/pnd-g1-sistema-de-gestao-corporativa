# módulo de relatórios de funcionarios
# funcionarios/relatorios.py

from .cadastro import funcionarios

def gerar_relatorio_funcionarios():
    print("Relatório de Funcionários: ")
    for funcionario in funcionarios:
        print(f"Nome: {funcionario['nome']}, Cargo: {funcionario['cargo']}, Salário: R$ {funcionario['salario']:.2f}")