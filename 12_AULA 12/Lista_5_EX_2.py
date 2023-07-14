titulo = 'Criação de Codinome'
'''
Data: 17/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Cria um codinome com os primeiros 3
caracteres e os ultimos 3 caracteres do nome
'''
print('Seja bem vindo ao programa ' + titulo)

def codinome(_nome):
    return _nome[:3] + _nome[-3:]

nome = input('Digite seu nome: ')

print(codinome(nome))