import random
from time import sleep

titulo = 'Jogo de luta'
'''
Data: 08/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Jogo de luta entre usuario
e PC
'''
print('Bem vindo ao programa ' + titulo)
print()
vida_usuario = 10
vida_pc = 10
sleep(1)
while True:
    print('Escolha (S) para utilizar o Soco, (C) para Cabeçada\n\
(I) para Informações ou (X) para Sair')
    escolha = input().upper()
    sleep(1)
    if escolha == 'S':
        print('Você escolheu utilizar o golpe Soco')
        poder_usuario = random.randint(1,6)
    elif escolha == 'C':
        print('Você escolheu utilizar o golpe Cabeçada')
        poder_usuario = 4
    elif escolha == 'I':
        print('\n' + '#'*40)
        sleep(0.3)
        print('S --> Soco: Desfere um soco no oponente')
        sleep(0.3)
        print('      Poder: D6')
        sleep(0.3)
        print('      Dano: D6\n')
        sleep(0.3)
        print('C --> Cabeçada: Ataca o oponente com uma cabeçada')
        sleep(0.3)
        print('      Poder: 4')
        sleep(0.3)
        print('      Dano: 3')
        sleep(0.3)
        print('      OBS: Caso consiga atacar, recebe 1 de dano')
        sleep(0.3)
        print('#' * 40 + '\n')
        continue
    elif escolha == 'X':
        print('Finalizando o Jogo')
        break
    else:
        print('Opção inválida')
        continue

    sleep(1)
    print('O PC irá utilizar o golpe Soco\n')
    poder_pc = random.randint(1,6)
    sleep(1)
    print('O seu poder de combate é ' + str(poder_usuario))
    sleep(0.5)
    print('O poder de combate do PC é ' + str(poder_pc) + '\n')

    sleep(2)
    if poder_usuario > poder_pc:
        print('Você venceu este combate')
        sleep(1)
        if escolha == 'S':
            dano = random.randint(1,6)
            print('O seu dano é ' + str(dano))
            vida_pc -= dano
        else:
            dano = 3
            print('O seu dano é ' + str(dano))
            vida_pc -= dano
            vida_usuario -= 1
            sleep(0.5)
            print('Você recebeu 1 de dano por utilizar o golpe Cabeçada')
    elif poder_usuario < poder_pc:
        print('Você perdeu este combate')
        sleep(1)
        dano = random.randint(1, 6)
        print('Você recebeu ' + str(dano) + ' de dano')
        vida_usuario -= dano
    else:
        print('Este combate empatou')

    sleep(1)
    print('\n' + '#' * 40)
    print('Jogador: ' + str(vida_usuario))
    print('PC: ' + str(vida_pc))
    print('#' * 40 + '\n')

    sleep(1)
    if vida_usuario <= 0:
        print('Você perdeu o jogo!!!')
        break
    elif vida_pc <= 0:
        print('Você venceu o jogo!!!')
        break