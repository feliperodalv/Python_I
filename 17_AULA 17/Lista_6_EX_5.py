titulo = 'Macro teclado'
'''
Data: 20/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Cria uma macro de teclado
ativada pelo botão do meio do mouse
'''
print('Bem vindo ao programa ' + titulo + '\n')
import keyboard
import mouse
import time

while True:
    if mouse.is_pressed('middle'):
        tempo = 1
        keyboard.press('w')
        time.sleep(tempo)
        keyboard.release('w')
        keyboard.press('a')
        time.sleep(tempo)
        keyboard.release('a')
        keyboard.press('s')
        time.sleep(tempo)
        keyboard.release('s')
        keyboard.press('d')
        time.sleep(tempo)
        keyboard.release('d')
        keyboard.press('w')
        time.sleep(tempo)
        keyboard.release('w')
