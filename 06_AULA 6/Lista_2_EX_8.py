titulo = 'Caixa Eletrônico'
'''
Data: 02/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Separa notas de um caixa eletrônico
sempre utilizando as notas de maior valor
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe quanto você quer sacar')
valor = int(input())

valor_restante = valor

notas_200 = valor_restante // 200
valor_restante = valor_restante - notas_200*200

notas_100 = valor_restante // 100
valor_restante = valor_restante - notas_100*100

notas_50 = valor_restante // 50
valor_restante = valor_restante - notas_50*50

notas_20 = valor_restante // 20
valor_restante = valor_restante - notas_20*20

notas_10 = valor_restante // 10
valor_restante = valor_restante - notas_10*10

notas_5 = valor_restante // 5
valor_restante = valor_restante - notas_5*5

notas_2 = valor_restante // 2
valor_restante = valor_restante - notas_2*2

notas_1 = valor_restante // 1
valor_restante -= valor_restante - notas_1*1

print('Você solicitou: R$' + str(valor))
if notas_200 > 0:
    print('Notas de 200 reais: ' + str(notas_200))
if notas_100 > 0:
    print('Notas de 100 reais: ' + str(notas_100))
if notas_50 > 0:
    print('Notas de 50 reais: ' + str(notas_50))
if notas_20 > 0:
    print('Notas de 20 reais: ' + str(notas_20))
if notas_10 > 0:
    print('Notas de 10 reais: ' + str(notas_10))
if notas_5 > 0:
    print('Notas de 5 reais: ' + str(notas_5))
if notas_2 > 0:
    print('Notas de 2 reais: ' + str(notas_2))
if notas_1 > 0:
    print('Notas de 1 reais: ' + str(notas_1))