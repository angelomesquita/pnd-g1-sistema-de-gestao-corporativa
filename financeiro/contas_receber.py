# módulo de de contas a receber da empresa
# financeiro/contas_receber.py

contas_receber = []

def registrar_conta(valor, descricao):
    conta = {"valor": valor, "descricao": descricao}
    contas_receber.append(conta)
    print(f"Conta a receber '{descricao}' registrada no valor de R$ {valor:.2f}")