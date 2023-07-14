titulo = 'Validação 2 Digitos CPF'
'''
Data: 12/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Valida os 2 digitos do CPF
que o usuario digitou
'''
print('Seja bem vindo ao programa ' + titulo)

def nome_mon(_nome):
    return _nome[0:4] + 'mon'

print('Por favor, digite seu nome')
nome = input('Nome: ')
print(nome_mon(nome))