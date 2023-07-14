titulo = 'Calculadora de IMC'
'''
Data: 27/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Calcula o IMC e informa ao usuário
'''

print('Bem vindo ao programa ' + titulo)


print('Por favor, informe seu nome')
nome = input()

print('Informe sua idade')
idade = int(input())

print('Informe seu peso em Kg')
peso = float(input())

print('Informe sua altura em metros')
altura = float(input())

num_caracteres = len(nome)

ano_nascimento = 2023 - idade

altura_em_cm = int(altura * 100)

imc = peso / (altura * altura)

print('Seu nome é ' + nome + ' e \
tem ' + str(num_caracteres) + ' caracteres,\
 você tem ' + str(idade) + ' anos e nasceu no\
 ano de ' + str(ano_nascimento) + '. Você mede\
 ' + str(altura_em_cm) + ' cm, pesa '+ str(peso) + ' Kg \
 e seu IMC é: ' + str(imc) + '.')