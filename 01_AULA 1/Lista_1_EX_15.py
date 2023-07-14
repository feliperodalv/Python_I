titulo = 'Calculadora de Media de Notas'
'''
Data: 27/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Calcula a média de duas notas
informadas pelo usuário
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe a primeira nota: ')
nota_1 = float(input())

print('Informe a segunda nota')
nota_2 = float(input())

media = (nota_1 + nota_2) / 2

print('A média das notas é ' + str(media))