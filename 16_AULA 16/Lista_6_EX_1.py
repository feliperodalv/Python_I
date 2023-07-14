titulo = 'Ola mundo'
'''
Data: 23/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Completa com " mundo" ao digitar "ola"

'''
print('Seja bem vindo ao programa ' + titulo)

import keyboard
texto = ''

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        letra = event.name
        if letra.isalpha() and len(letra) == 1:
            texto += letra

        if letra == 'space':
            if texto == 'ola':
                keyboard.write('mundo')
            texto = ''
        if letra == 'backspace':
            texto = texto[0:-1]