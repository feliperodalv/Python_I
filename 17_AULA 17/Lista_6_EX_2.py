titulo = 'Desenha Letra'
'''
Data: 23/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Desenha a primeira letra
do nome ao clicar ctrl

'''
print('Seja bem vindo ao programa ' + titulo)

import keyboard
import mouse
while True:
    if keyboard.is_pressed('ctrl'):
        # Para desenhar o D com arco
        x = 0
        x_old = 0
        delta = 10
        mouse.drag(0, 0, 0, 13 * delta, absolute=False, duration=0.1)
        for y in range(0, 22 * delta, 1):
            x = -0.1 * delta * y ** 2 + 1 * delta * y + 2 * delta
            if x < 0: x = 0
            mouse.drag(0, 0, x - x_old, -1 * delta, absolute=False, duration=0.01)
            x_old = x
            if x == 0: break

        # Para desenhar varios Ds com arco
        '''step = -1
        for delta in range(30,1,step):
            mouse.drag(-step*2, -step * 6.3, 0, 13 * delta, absolute=False, duration=0.1)
            for y in range(0, 22*delta, 1):
                x = -0.1*delta * y ** 2 + 1 * delta * y + 2 * delta
                print('xy: ', x, y)
                if x < 0: x = 0
                mouse.drag(0, 0, x - x_old, -1 * delta, absolute=False, duration=0.01)
                x_old = x
                if x == 0: break'''

        # Para desenhar D com retas
        '''mouse.drag(0, 0, 50, -50, absolute=False, duration=0.1)
        mouse.drag(0, 0, 25, -50, absolute=False, duration=0.1)
        mouse.drag(0, 0, -25, -50, absolute=False, duration=0.1)
        mouse.drag(0, 0, -50, -50, absolute=False, duration=0.1)'''