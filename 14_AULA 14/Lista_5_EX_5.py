titulo = 'Deslocador de texto'
'''
Data: 18/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Desloca cada palavra de um texto
informado pelo usuario
'''
print('Seja bem vindo ao programa ' + titulo)

'''
def deslocador_de_texto(_texto):
    palavras = _texto.split(' ')
    texto_invertido = ''
    for palavra in palavras:
        if len(palavra) >= 3:
            texto_invertido += palavra[-3:] + palavra[0:-3] + ' '
        else:
            texto_invertido += palavra[-1:] + palavra[0:-1] + ' '
    return texto_invertido
'''

def deslocador_de_texto(_texto, desloc = 3):
    palavras = _texto.split(' ')
    texto_invertido = ''

    for palavra in palavras:
        if len(palavra) >= desloc:
            texto_invertido += palavra[-desloc:] + palavra[0:-desloc] + ' '
        else:
            desloc_2 = desloc % len(palavra)
            texto_invertido += palavra[-desloc_2:] + palavra[0:-desloc_2] + ' '

    return texto_invertido


texto = input('Digite um texto: ')

print(deslocador_de_texto(texto))

print(deslocador_de_texto('hora do intervalo', 7))