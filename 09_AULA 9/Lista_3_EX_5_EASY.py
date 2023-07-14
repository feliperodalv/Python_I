titulo = 'Jogo da Forca'
'''
Data: 08/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Jogo da Forca
'''
print('Bem vindo ao programa ' + titulo)

palavra_secreta = input('Palavra secreta: ').upper()
dica = input('Dica: ')
tentativas = 10
letras_tentativa = ''

palavra_descoberta = ''
for letra in palavra_secreta:
    if letra == ' ' or letra == '-':
        palavra_descoberta += letra
    else:
        palavra_descoberta += '_'

print('\n' * 50)

print('O jogo da Forca começou')

while True:
    print('\n' + '#' * 40)
    print('Palavra: ' + palavra_descoberta)
    print('Dica: ' + dica)
    print('Letras digitadas: ', end='')
    for letra in letras_tentativa:
        print(letra + ' ',end='')
    print('\nTentativa: ' + str(tentativas))


    letra_digitada = input('Digite uma letra: ').upper()

    if len(letra_digitada) > 1:
        print('Digite apenas 1 letra')
        continue
    if letra_digitada in letras_tentativa:
        print('Você já digitou esta letra')
        continue


    letras_tentativa += letra_digitada
    palavra_alterada = ''
    achou_letra = False
    if letra_digitada in palavra_secreta:
        for indice_secreto, letra_secreta in enumerate(palavra_secreta):
            if letra_digitada == letra_secreta:
                palavra_alterada += letra_secreta
                achou_letra = True
            else:
                palavra_alterada += palavra_descoberta[indice_secreto]

    if achou_letra == False:
        tentativas -= 1
        print('Letra não encontrada')
    else:
        palavra_descoberta = palavra_alterada

    if tentativas <= 0:
        print('Você perdeu o jogo')
        print('A palavra secreta era ' + palavra_secreta)
        break

    if palavra_descoberta == palavra_secreta:
        print('Você venceu o jogo')
        break
    print('\n' + '#' * 40 + '\n')
