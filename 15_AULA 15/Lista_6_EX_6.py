titulo = 'Gravador de Macro Mouse'
'''
Data: 20/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Cria um gravador de macro
que inicia ao clicar CTRL e finaliza ao clicar CTRL
salva em um arquivo CSV
'''
print('Bem vindo ao programa ' + titulo + '\n')

import csv
import mouse
import keyboard
import time

gravador = False
macro = []
while True:
    if keyboard.is_pressed('ctrl'):
        gravador = not gravador
        time.sleep(0.5)
        if gravador:
            print('Gravando')
        else:
            print('Finalizando gravação')
            if len(macro) > 0:
                print(macro)
                with open('Arquivos/macro.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    for linha in macro:
                        writer.writerow(linha)

                break
    if gravador == True:
        if mouse.is_pressed('left'):
            linha = []
            linha.append('left')
            linha.append(mouse.get_position())
            macro.append(linha)
            time.sleep(0.2)
        elif mouse.is_pressed('middle'):
            linha = []
            linha.append('middle')
            linha.append(mouse.get_position())
            macro.append(linha)
            time.sleep(0.2)
        elif mouse.is_pressed('right'):
            linha = []
            linha.append('right')
            linha.append(mouse.get_position())
            macro.append(linha)
            time.sleep(0.2)