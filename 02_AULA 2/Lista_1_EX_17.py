titulo = 'Calculadora de Latas de Tinta'
'''
Data: 27/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Calcula quantas latas de tinta
o usuário precisa a partir da altura e largura
da parede informada pelo usuário
'''
print('Bem vindo a loja TINTAS e AGUARAIZ LTDA')

print('''Este programa irá calcular quantas latas
de tintas SUVEUNIL você precisará para 
pintar!!!
''')

print('Por favor informe a altura em metros')
altura = float(input())

print('Informe a largura em metros')
largura = float(input())

area = altura * largura

area_lata = 3

latas_inteiro = area // area_lata

resto = area % area_lata

tem_resto = resto > 0

latas_total = int(latas_inteiro + tem_resto)

print('Para pintar a uma area de ' + str(area) + ' m² \
você precisará de ' + str(latas_total) + ' Latas de Tinta\
 SUVEUNIL')
