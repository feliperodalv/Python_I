titulo = 'Adivinhe o número'
'''
Data: 04/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Jogo para adivinhar um número
de 0 a 10000
'''
print('Bem vindo ao programa ' + titulo)

import random

numero_secreto = random.randint(0,10000)
print('Adivinhe o numero secreto entre 0 e 10000')
#print(numero_secreto)

melhor_chute = 100000

for tentativa in range(1,11):
    print('\n' + '#'*40)
    print('Tentativa: ' + str(tentativa))
    numero = int(input('Digite um número: '))

    if abs(numero_secreto - numero) < abs(numero_secreto - melhor_chute):
        melhor_chute = numero

    if numero_secreto == numero:
        print('Você acertou!!!')
        break
    elif tentativa < 10:
        if numero_secreto > numero:
            print('Digite um número maior')
        else:
            print('Digite um número menor')
else:
    print('\nVocê perdeu!!! O número era ' + str(numero_secreto))
    print('Sua melhor tentativa foi ' + str(melhor_chute))
    print('Você errou por ' + str(abs(numero_secreto - melhor_chute)))