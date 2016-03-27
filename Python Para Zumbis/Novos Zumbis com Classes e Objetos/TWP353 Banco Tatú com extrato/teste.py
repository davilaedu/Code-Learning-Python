import TWP352b
import TWP353

joao = TWP352b.Cliente('Joao da Silva', '777-1234')
maria = TWP352b.Cliente('Maria da Silva', '555-4321')
conta11 = TWP353.Conta(joao.nome, 1)

print conta11.clientes
conta11.deposito(500)
conta11.deposito(300)
conta11.deposito(95)
conta11.saque(250)

print conta11.extrato()
