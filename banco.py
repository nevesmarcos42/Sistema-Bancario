class Banco:
    def __init__(self):
        self.saldo = 0
        self.limite_saque = 500
        self.limite_saques_diarios = 3
        self.saques_hoje = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite_saque:
            print("Valor de saque excede o limite permitido.")
        elif self.saques_hoje >= self.limite_saques_diarios:
            print("Limite de saques diários excedido.")
        else:
            self.saldo -= valor
            self.saques_hoje += 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R$ {self.saldo:.2f}")

    def resetar_saques_diarios(self):
        self.saques_hoje = 0
        print("Contador de saques diários resetado.")

    def mostrar_extrato(self):
        print("Extrato:")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Exemplo de uso
banco = Banco()
banco.depositar(1000)
banco.sacar(200)
banco.sacar(300)
banco.sacar(100)
banco.consultar_saldo()
banco.resetar_saques_diarios()
banco.sacar(500)
banco.consultar_saldo()
banco.mostrar_extrato()
