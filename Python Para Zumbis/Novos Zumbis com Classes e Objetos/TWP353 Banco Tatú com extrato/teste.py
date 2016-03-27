import TWP352b
from TWP353 import Conta

joao = TWP352b.Cliente('Joao da Silva', '777-1234')
maria = TWP352b.Cliente('Maria da Silva', '555-4321')
conta11 = Conta(joao.nome, 1, 1000)
conta22 = Conta(maria.nome, 2)
print conta11.clientes

conta11.saque(50)
conta11.saque(190)
print conta11.extrato()
