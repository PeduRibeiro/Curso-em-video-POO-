class ContaBancaria:
    """
    Cria uma conta e permite saques e depositos

    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta Bancaria: {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo"

    def deposito(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:,.2f} autorizado na conta {self.id}\n")

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}\n")
        else:
            print(f"O Saque de {valor:,.2f} foi recusado por falta de saldo na conta {self.id}\n.")


c1 = ContaBancaria(112, "Gustavo", 3000)
c1.deposito(500)
c1.saque(20000)
print(c1)