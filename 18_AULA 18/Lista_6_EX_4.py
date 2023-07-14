titulo = 'Lista de Compras'
'''
Data: 24/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Lista de compras com a possibilidade
de gravar em arquivo
'''
print('Seja bem vindo ao programa ' + titulo)
import csv

lista_de_compras = []

try:
    with open('Arquivos/compras.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for linha in reader:
            lista_de_compras.append(linha)
except:
    pass

while True:
    print('Escolha uma das opções: ')
    print('I --> Inserir')
    print('D --> Deletar')
    print('L --> Listar')
    print('S --> Salvar')
    print('X --> Sair')
    escolha = input('Escolha: ').upper()

    if escolha == 'I':
        while True:
            produto = []
            print('Digite (Q) para voltar ou o item para inserir')
            item = input('Item a ser inserido: ').upper()
            if item == 'Q':
                print('Voltando ao menu...')
                break
            else:
                try:
                    quantidade = float(input('Quantidade: '))
                    if quantidade > 0:
                        produto.append(item)
                        produto.append(quantidade)
                        item_existente = False
                        for produto_lista, quant_lista in lista_de_compras:
                            if item == produto_lista:
                                item_existente = True
                                print('Este item já foi inserido anteriormente')
                                break

                        if item_existente == True:
                            continue
                        else:
                            lista_de_compras.append(produto)
                            print('Item cadastrado com sucesso')
                    else:
                        print('Quantidade inválida')
                except:
                    print('Quantidade inválida')
    elif escolha == 'D':
        print('Lista de Compras:')
        for indice, produto in enumerate(lista_de_compras, start=1):
            print(indice, '-->',end=' ')
            print(produto[0], produto[1], sep=' - ')
        deletar = int(input('Numero do Item: '))
        del lista_de_compras[deletar-1]
        print('Item deletado')
    elif escolha == 'L':
        print('Lista de Compras:')
        for indice, produto in enumerate(lista_de_compras, start=1):
            print(indice, '-->', end=' ')
            print(produto[0], produto[1], sep=' - ')
    elif escolha == 'S':
        print('Salvando arquivo')
        with open('Arquivos/compras.csv','w',newline='') as file:
            writer = csv.writer(file)
            for produto in lista_de_compras:
                writer.writerow(produto)
    elif escolha == 'X':
        print('Saindo do programa')
        break
    else:
        print('Escolha uma opção válida')