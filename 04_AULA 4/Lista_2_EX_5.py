titulo = 'Reajuste Salarial'
'''
Data: 02/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Calcula o reajuste salarial com
base nos seguintes critérios:
•	Salário Abaixo de R$1.500,00  Aumento de 25%
•	Salário Entre de R$1.500,00 e R$1.999,99  Aumento de 20%
•	Salário Entre de R$2.000,00 e R$2.999,99  Aumento de 15%
•	Salário Entre de R$3.000,00 e R$4.999,99  Aumento de 10%
•	Salário Igual ou Acima de R$5.000,00  Aumento de 5%
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe seu salário atual')

salario_atual = float(input())

if salario_atual < 1500:
    aumento = 25
elif salario_atual < 2000:
    aumento = 20
elif salario_atual < 3000:
    aumento = 15
elif salario_atual < 5000:
    aumento = 10
else:
    aumento = 5

aumento_em_reais = salario_atual * aumento / 100
salario_final = salario_atual + aumento_em_reais

print('Seu salário atual é R$' + str(salario_atual))
print('Você irá receber ' + str(aumento) + '% de aumento')
print('Seu reajuste será de R$' + str(aumento_em_reais))
print('Seu salário será ajustado para R$' + str(salario_final))
