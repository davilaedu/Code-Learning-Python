from TWP352 import Cliente
from TWP352 import Conta


joao = Cliente('Joao da Silva', '777-1234')
maria = Cliente('Maria da Silva', '555-4321')
print joao.nome
print joao.telefone
print ('Nome: %s e Telefone: %s' % (joao.nome, joao.telefone))
print ('Nome: %s e Telefone: %s' % (maria.nome, maria.telefone))
conta1 = Conta(joao.nome, 1, 1000)
conta2 = Conta(maria.nome, 1, 1000)
print conta1.resumo()
print conta2.resumo()
