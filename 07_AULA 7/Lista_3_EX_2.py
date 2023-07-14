import random

titulo = 'Jogar dois dados'
'''
Data: 04/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Faz o lance de dois dados com o
número de jogadas informadas pelo usuário
'''
print('Bem vindo ao programa ' + titulo)

resultado_2 = 0
resultado_3 = 0
resultado_4 = 0
resultado_5 = 0
resultado_6 = 0
resultado_7 = 0
resultado_8 = 0
resultado_9 = 0
resultado_10 = 0
resultado_11 = 0
resultado_12 = 0

print('Por favor, informe o número de vezes que quer jogar os dados')

vezes = int(input())

for vez in range(vezes):
    dado_1 = random.randint(1,6)
    dado_2 = random.randint(1,6)
    soma = dado_1 + dado_2

    if soma == 2:
        resultado_2 += 1
    elif soma == 3:
        resultado_3 += 1
    elif soma == 4:
        resultado_4 += 1
    elif soma == 5:
        resultado_5 += 1
    elif soma == 6:
        resultado_6 += 1
    elif soma == 7:
        resultado_7 += 1
    elif soma == 8:
        resultado_8 += 1
    elif soma == 9:
        resultado_9 += 1
    elif soma == 10:
        resultado_10 += 1
    elif soma == 11:
        resultado_11 += 1
    elif soma == 12:
        resultado_12 += 1


print('Resultado 2: ' + str(resultado_2))
print('Resultado 3: ' + str(resultado_3))
print('Resultado 4: ' + str(resultado_4))
print('Resultado 5: ' + str(resultado_5))
print('Resultado 6: ' + str(resultado_6))
print('Resultado 7: ' + str(resultado_7))
print('Resultado 8: ' + str(resultado_8))
print('Resultado 9: ' + str(resultado_9))
print('Resultado 10: ' + str(resultado_10))
print('Resultado 11: ' + str(resultado_11))
print('Resultado 12: ' + str(resultado_12))

maior_probabilidade = -1
melhor_resultado = -1

if maior_probabilidade < resultado_2:
    maior_probabilidade = resultado_2
    melhor_resultado = 2
if maior_probabilidade < resultado_3:
    maior_probabilidade = resultado_3
    melhor_resultado = 3
if maior_probabilidade < resultado_4:
    maior_probabilidade = resultado_4
    melhor_resultado = 4
if maior_probabilidade < resultado_5:
    maior_probabilidade = resultado_5
    melhor_resultado = 5
if maior_probabilidade < resultado_6:
    maior_probabilidade = resultado_6
    melhor_resultado = 6
if maior_probabilidade < resultado_7:
    maior_probabilidade = resultado_7
    melhor_resultado = 7
if maior_probabilidade < resultado_8:
    maior_probabilidade = resultado_8
    melhor_resultado = 8
if maior_probabilidade < resultado_9:
    maior_probabilidade = resultado_9
    melhor_resultado = 9
if maior_probabilidade < resultado_10:
    maior_probabilidade = resultado_10
    melhor_resultado = 10
if maior_probabilidade < resultado_11:
    maior_probabilidade = resultado_11
    melhor_resultado = 11
if maior_probabilidade < resultado_12:
    maior_probabilidade = resultado_12
    melhor_resultado = 12

chance = maior_probabilidade * 100 / vezes
print('\nA maior probabilidade é de cair o resultado ' + str(melhor_resultado))
print('Este resultado caiu ' + str(maior_probabilidade) + ' vezes')
print('A chance de cair este resultado é de ' + str(chance) + '%')