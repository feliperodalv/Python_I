titulo = 'Pedra, Papel e Tesoura'
'''
Data: 05/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Jogo da Pedra, Papel e Tesoura
'''
print('Bem vindo ao programa ' + titulo)

import random
from time import sleep

num_vit = 0
num_emp = 0
num_der = 0

while True:
    print('Escolha (R) para Pedra, (P) para Papel, \
(T) para Tesoura ou (X) para Sair')

    escolha = input('Escolha: ').upper()

    if escolha == 'X':
        print('Finalizando o jogo')
        sleep(1)
        break
    elif escolha == 'R':
        escolha_texto = 'Pedra'
    elif escolha == 'P':
        escolha_texto = 'Papel'
    elif escolha == 'T':
        escolha_texto = 'Tesoura'
    else:
        print('Você digitou algo inválido')
        sleep(1)
        continue

    print('\nVocê jogou ...')
    sleep(0.5)
    print(escolha_texto)

    escolha_pc = random.randint(1,3)
    if escolha_pc == 1:
        escolha_pc = 'R'
    elif escolha_pc == 2:
        escolha_pc = 'P'
    elif escolha_pc == 3:
        escolha_pc = 'T'
    sleep(1)

    print('\nO PC jogou ...')
    sleep(0.5)
    if escolha_pc == 'R':
        print('Pedra')
    elif escolha_pc == 'P':
        print('Papel')
    elif escolha_pc == 'T':
        print('Tesoura')

    sleep(1)
    print('\nResultado do jogo ...')
    sleep(1.5)
    if escolha == 'R' and escolha_pc == 'R':
        print('Empatou!!!')
        num_emp += 1
    elif escolha == 'R' and escolha_pc == 'P':
        print('Perdeu!!!')
        num_der += 1
    elif escolha == 'R' and escolha_pc == 'T':
        print('Ganhou!!!')
        num_vit +=1

    elif escolha == 'P' and escolha_pc == 'R':
        print('Ganhou!!!')
        num_vit += 1
    elif escolha == 'P' and escolha_pc == 'P':
        print('Empatou!!!')
        num_emp += 1
    elif escolha == 'P' and escolha_pc == 'T':
        print('Perdeu!!!')
        num_der += 1

    elif escolha == 'T' and escolha_pc == 'R':
        print('Perdeu!!!')
        num_der += 1
    elif escolha == 'T' and escolha_pc == 'P':
        print('Ganhou!!!')
        num_vit += 1
    elif escolha == 'T' and escolha_pc == 'T':
        print('Empatou!!!')
        num_emp += 1

    sleep(1)
    print('\n' + '#'*40)
    sleep(0.5)
    print('Vitórias: ' + str(num_vit))
    sleep(0.5)
    print('Empates: ' + str(num_emp))
    sleep(0.5)
    print('Derrotas: ' + str(num_der))
    sleep(0.5)
    print('#' * 40 + '\n' )
    sleep(1)