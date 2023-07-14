titulo = 'Listagem de string'
'''
Data: 29/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Separa uma string em lista
e enumera
'''
print('Seja bem vindo ao programa ' + titulo)

texto = '''jose
jorge
maria
antonio
ana
julia
márcio
fernando
zelia'''

lista = texto.split('\n')
#lista = texto.splitlines()
print(lista)
#for item in lista:
#    print(item)

for indice, item in enumerate(lista,start=1):
    print(indice,'-',item)
