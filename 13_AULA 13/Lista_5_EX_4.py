titulo = 'Inverte um texto'
'''
Data: 18/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Inverte um texto informado pelo usuario
'''
print('Seja bem vindo ao programa ' + titulo)

def inversor(_texto):
    texto_invertido = ''
    # range (start, stop, step) -- começa no final do texto
    # termina no indice 0 e faz cada passo de -1 em -1
    for indice in range(len(_texto) - 1, -1, -1):
        texto_invertido += _texto[indice]
    return texto_invertido



texto = input('Digite um texto: ')

print(inversor(texto))