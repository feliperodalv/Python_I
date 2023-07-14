titulo = 'Par ou Impar'
'''
Data: 28/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Verifica se um número informado
pelo usuário é par ou ímpar
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe um número')
numero = int(input())

if numero % 2 == 0:
    print('O número informado é par')
else:
    print('O número informado é ímpar')
