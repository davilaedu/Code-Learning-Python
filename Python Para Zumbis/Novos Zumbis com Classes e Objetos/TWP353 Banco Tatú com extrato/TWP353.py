class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print ('CC N%s Saldo: %.2f' % (self.numero, self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['Saque', valor])

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['Deposito', valor])

    def extrato(self):
        print ('Extrato CC N %s' % self.numero)
        for op in self.operacoes:
            print ('%s %.2f' % (op[0], op[1]))
        print ('%s %.2f' % ('Saldo = ', self.saldo))
