titulo = 'Utilizador de Macro Mouse'
'''
Data: 20/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Utiliza a Macro gravada no EX 6
após pressionar a tecla CTRL
'''
print('Bem vindo ao programa ' + titulo + '\n')
import csv
import mouse
import keyboard
import time

macro = []
with open('Arquivos/macro.csv','r') as file:
    reader = csv.reader(file)
    for linha in reader:
        macro.append(linha)

while True:
    if keyboard.is_pressed('ctrl'):
        time.sleep(0.2)
        print('Executando Macro')
        for linha in macro:
            lista_move = linha[1].split(',')
            x_move = int(lista_move[0][1:])
            y_move = int(lista_move[1][0:-1])
            mouse.move(x_move,y_move,duration=1)
            mouse.click(linha[0])
