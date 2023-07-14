titulo = 'Oticas Carolina'
'''
Data: 02/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: calcula o desconto de um oculos
de 200 reais com limites de 10 a 80%
de desconto
'''
print('Bem vindo ao programa ' + titulo)

print('Parabéns!!! Você acaba de ganhar um desconto especial')

print('Para adquiri-lo, digite sua idade')

valor_oculos = 200

idade = int(input())

if idade < 10:
    desconto = 10
elif idade > 80:
    desconto = 80
else:
    desconto = idade

desconto_em_reais =  valor_oculos * desconto / 100

valor_final = valor_oculos - desconto_em_reais

print('Você ganhou ' + str(desconto) + '% de desconto')
print('O óculos que sairia por R$' + str(valor_oculos) + ' reais')
print('Irá sair por apenas R$' + str(valor_final) + ' reais')
print('Você obteve R$' + str(desconto_em_reais) + ' reais de desconto')
