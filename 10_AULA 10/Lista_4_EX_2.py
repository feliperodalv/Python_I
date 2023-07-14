titulo = 'Lista de Compras'
'''
Data: 29/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Cria uma lista com
a possibilidade de inserir
deletar e listar
'''
print('Seja bem vindo ao programa ' + titulo)

compras = []

while True:
    print('Escolha uma das opções: ')
    print('I --> Inserir')
    print('D --> Deletar')
    print('L --> Listar')
    print('X --> Sair')
    escolha = input('Escolha: ').upper()

    if escolha == 'I':
        while True:
            print('Digite (Q) para voltar ou o item para inserir')
            item = input('Item a ser inserido: ').upper()
            if item == 'Q':
                print('Voltando ao menu...')
                break
            else:
                if item in compras:
                    print('Este item já foi inserido anteriormente')
                else:
                    compras.append(item)
    elif escolha == 'D':
        print('Lista:')
        for indice, item in enumerate(compras, start=1):
            print(indice, '-', item)
        deletar = int(input('Numero do Item: '))
        del compras[deletar-1]
        print('Item deletado')
    elif escolha == 'L':
        print('Lista:')
        for indice, item in enumerate(compras, start=1):
            print(indice, '-', item)
    elif escolha == 'X':
        print('Saindo do programa')
        break
    else:
        print('Escolha uma opção válida')