# Arquivo principal

from funcionarios import cadastro as func_cadastro
from funcionarios import folha_pagamento as func_folha
from funcionarios import relatorios as func_relatorios
from financeiro import contas_pagar as fin_contas_pagar
from financeiro import contas_receber as fin_contas_receber
from financeiro import relatorios as fin_relatorios

def main():
    print("Bem-vindo ao Sistema de Gestão Corporativa")
    
    print(f"\n--- Funcionários ---")
    func_cadastro.cadastrar_funcionario("João", "Desenvolvedor", 5000)
    func_cadastro.cadastrar_funcionario("Maria", "Desenvolvedora", 6000)
    func_cadastro.cadastrar_funcionario("Jose", "Desenvolvedor", 4000)
    func_folha.calcular_salarios()
    func_relatorios.gerar_relatorio_funcionarios()

    print(f"\n--- Financeiro ---")
    fin_contas_pagar.registrar_conta(1000, "Aluguel")
    fin_contas_pagar.registrar_conta(500, "Energia")
    fin_contas_receber.registrar_conta(8000, "Cliente A")
    fin_contas_receber.registrar_conta(6000, "Cliente B")
    fin_relatorios.gerar_relatorio_financeiro()

if __name__ == "__main__":
    main()