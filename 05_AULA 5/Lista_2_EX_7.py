titulo = 'Validação de Data'
'''
Data: 02/05/2023
Autor: Prof. MSc. Ailton Santos
Descrição: Valida se uma data é real
'''
print('Bem vindo ao programa ' + titulo)

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

if (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0)\
    or (ano % 4 == 0 and ano % 100 != 0):
    bissexto = True
else:
    bissexto = False

data_real = False

if ano > 0:
    if mes == 1 or mes == 3 or mes == 5\
        or mes == 7 or mes == 8 or mes == 10\
        or mes == 12:
        if dia >= 1 and dia <= 31:
            data_real = True
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            data_real = True
    elif mes == 2:
        if bissexto == True:
            if dia >= 1 and dia <= 29:
                data_real = True
        else:
            if dia >= 1 and dia <= 28:
                data_real = True

if data_real == True:
    print('A data informada é Válida')
else:
    print('A data informada Não Existe')