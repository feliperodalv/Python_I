titulo = 'Validação 2 Digitos CPF'
'''
Data: 12/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Valida os 2 digitos do CPF
que o usuario digitou
'''
print('Seja bem vindo ao programa ' + titulo)

while True:
    cpf = input('Digite seu CPF: ')
    cpf = cpf.replace('.','')
    cpf = cpf.replace('-','')

    if len(cpf) != 11 or not cpf.isdecimal():
        print('CPF Inválido, digite novamente')

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
        print('Validando 2º digito do CPF')
        indice = 0

        soma = 0

        for numero in range(11, 1, -1):
            print(numero, 'x', cpf[indice], '=', numero * int(cpf[indice]))
            soma += numero * int(cpf[indice])
            indice += 1

        print('Soma_2: ', soma)
        soma *= 10
        print('Soma_2 x 10:', soma)

        resultado = soma % 11

        print('resultado 2:', resultado)

        if resultado > 9:
            resultado = 0

        print('resultado 2:', resultado)

        if resultado == int(cpf[10]):
            print('2º Digito do CPF está correto')
        else:
            print('CPF Inválido')
    else:
        print('CPF Inválido')