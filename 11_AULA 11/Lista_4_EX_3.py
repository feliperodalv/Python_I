titulo = 'Validação 1º Digito CPF'
'''
Data: 29/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Valida o 1º digito do CPF
que o usuario digitou
'''
print('Seja bem vindo ao programa ' + titulo)

while True:
    cpf = input('Digite seu CPF: ')
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-','')

    if len(cpf) != 11 or not cpf.isdecimal():
        print('CPF Inválido, digite novamente')
        continue


    print(cpf[2])
    indice = 0

    soma = 0

    for numero in range(10,1,-1):
        print(numero,'x',cpf[indice],'=',numero*int(cpf[indice]))
        soma += numero*int(cpf[indice])
        indice += 1

    print('Soma: ',soma)
    soma *= 10
    print('Soma x 10:',soma)

    resultado = soma % 11

    print('resultado:',resultado)

    if resultado > 9:
        resultado = 0

    print('resultado:',resultado)

    if resultado == int(cpf[9]):
        print('1º Digito do CPF está correto')
    else:
        print('CPF Inválido')