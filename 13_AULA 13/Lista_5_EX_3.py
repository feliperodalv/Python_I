titulo = 'Alteração de texto para numero'
'''
Data: 17/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Altera um texto seguindo o seguinte critério:
Letra A  4
Letra B  8
Letra E  3
Letra I  1
Letra O  0
Letra T  7
'''
print('Seja bem vindo ao programa ' + titulo)

'''def alterador_texto(_texto):
    _texto = _texto.upper()
    _texto = _texto.replace('A', '4')
    _texto = _texto.replace('B', '8')
    _texto = _texto.replace('E', '3')
    _texto = _texto.replace('I', '1')
    _texto = _texto.replace('O', '0')
    _texto = _texto.replace('T', '7')
    return _texto


texto = input('Digite um texto: ').upper()

print(alterador_texto(texto))
'''
lista_normal = ['A','B','E','I','O','T']
lista_alterada = ['4','8','3','1','0','7']

def alterador_texto(_texto):
    _texto = _texto.upper()
    for indice, letra in enumerate(lista_normal):
        _texto = _texto.replace(letra, lista_alterada[indice])
    return _texto


texto = input('Digite um texto: ').upper()

print(alterador_texto(texto))
