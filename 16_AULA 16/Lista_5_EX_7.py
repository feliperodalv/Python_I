titulo = 'Lista de usuarios'
'''
Data: 18/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Cria uma lista de usuarios
com validação de CPF e possibilidade de
cadastrar, deletar e listar os usuarios

'''
print('Seja bem vindo ao programa ' + titulo)
lista_usuarios = []

def inserir_usuario(_nome,_idade,_cpf):
    usuario = {}
    usuario['nome'] = _nome.title()
    usuario['idade'] = _idade
    usuario['cpf'] = valida_cpf(_cpf)
    if usuario['cpf'] != '':
        valido = True
        for usuario_cad in lista_usuarios:
            if usuario_cad['cpf'] == usuario['cpf']:
                valido = False
                break

        if valido == False:
            return 'Usuario já cadastrado'
        else:
            lista_usuarios.append(usuario)
            return 'Cadastrado com sucesso'
    else:
        return 'Cadastro invalido'

def valida_cpf(_cpf, digito = 1):
    try:
        if not _cpf.isdecimal():
            if _cpf[3] != '.' or _cpf[7] != '.' or _cpf[11] != '-':
                return ''
            _cpf = _cpf.replace('.', '')
            _cpf = _cpf.replace('-', '')
        if len(_cpf) != 11 or not _cpf.isdecimal():
            return ''
    except:
        return ''
    indice = 0
    soma = 0
    for numero in range(digito+9, 1, -1):
        soma += numero * int(_cpf[indice])
        indice += 1
    soma *= 10
    resultado = soma % 11
    if resultado > 9:
        resultado = 0

    if resultado == int(_cpf[digito + 8]):
        if digito == 1:
            return valida_cpf(_cpf, 2)
        if digito == 2:
            return _cpf[0:3] + '.' + _cpf[3:6] + '.' + _cpf[6:9] + '-' + _cpf[9:]
    else:
        return ''

def listar_usuario():
    if len(lista_usuarios) == 0:
        print('Lista ainda não tem usuários cadastrados')
    else:
        print('\n\nLista de Usuários')
        for indice, usuario in enumerate(lista_usuarios, start=1):
            print(indice, '-', end=' ')
            for indice, dados in enumerate(usuario.items()):
                chave, valor = dados
                print(chave, ': ', valor, sep='', end='')
                if indice < len(usuario) - 1:
                    print('  |  ', end='')
            print()
        print('\n')

while True:
    print('''Escolha uma opção:
(C) para Cadastrar
(D) para Deletar
(L) para Listar
(X) para Sair''')
    escolha = input('Opção: ').upper()

    if escolha == 'C':
        try:
            nome = input('Digite o nome: ')
            idade = int(input('Digite a idade: '))
            cpf = input('Digite o CPF: ')
            print(inserir_usuario(nome, idade, cpf))
        except:
            print('Erro ao realizar cadastro')
    elif escolha == 'D':
        listar_usuario()
        try:
            numero = int(input('Escolha qual usuario deletar: '))
            if numero < 1:
                print('Erro ao deletar usuario, valor inválido')
            else:
                deletado = lista_usuarios.pop(numero - 1)
                print('O usuario',deletado['nome'],'foi deletado')
        except:
            print('Erro ao deletar usuario, valor inválido')
    elif escolha == 'L':
        listar_usuario()
    elif escolha == 'X':
        print('Finalizando programa')
        break
    else:
        print('Digite uma escolha válida')