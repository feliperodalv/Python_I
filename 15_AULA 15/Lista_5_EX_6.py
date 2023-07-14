titulo = 'Criar lista de usuarios'
'''
Data: 18/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Cria uma lista de usuarios
'''
print('Seja bem vindo ao programa ' + titulo)

lista_usuarios = []

def inserir_usuario(_nome,_idade):
    usuario = {}
    usuario['nome'] = _nome
    usuario['idade'] = _idade
    lista_usuarios.append(usuario)


nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))

inserir_usuario(nome,idade)
inserir_usuario('Joao',15)
inserir_usuario('Maria',40)

print(lista_usuarios)