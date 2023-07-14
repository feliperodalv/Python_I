titulo = 'Gratuidade'
'''
Data: 28/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Verifica a idade do usuário
e informa se tem gratuidade no transporte público
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe sua idade')
idade = int(input())

if idade >= 65:
    print('Pode passar de graça')
else:
    print('Pague R$5,00')
