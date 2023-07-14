titulo = 'Importação de Itens TXT'
'''
Data: 23/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Importa uma lista TXT
e retorna como CSV com a media
'''
print('Seja bem vindo ao programa ' + titulo)
import csv

with open('Arquivos/alunos.txt','r') as file:
    texto = file.read()

linhas = texto.split('\n')

lista_alunos = []

# trabalhando com lista de dicionarios
for linha in linhas:
    aluno = {}
    itens = linha.split(',')
    media = (float(itens[1]) + float(itens[2])) / 2
    aluno['nome'] = itens[0]
    aluno['nota1'] = itens[1]
    aluno['nota2'] = itens[2]
    aluno['media'] = media
    lista_alunos.append(aluno)

print(lista_alunos)



with open('Arquivos/alunos.csv', 'w', newline='') as file:
    lista = []
    for chave in lista_alunos[0].keys():
        lista.append(chave)
    writer = csv.DictWriter(file, fieldnames=lista)

    writer.writeheader()
    for aluno in lista_alunos:
        writer.writerow(aluno)




# trabalhando com lista de listas

'''for linha in linhas:
    aluno = []
    itens = linha.split(',')
    media = (float(itens[1]) + float(itens[2])) / 2
    aluno.append(itens[0])
    aluno.append(itens[1])
    aluno.append(itens[2])
    aluno.append(media)
    lista_alunos.append(aluno)


with open('Arquivos/alunos.csv','w',newline='') as file:
    writer = csv.writer(file)
    header = ['Nome','Nota 1', 'Nota 2', 'Media']
    writer.writerow(header)
    for aluno in lista_alunos:
        writer.writerow(aluno)'''
