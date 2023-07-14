titulo = 'Media de aluno'
'''
Data: 28/04/2023
Autor: Prof. MSc. Ailton Santos
Descrição: calcula a média a partir de 2
notas informadas pelo usuário e define
se o aluno está aprovado, reprovado ou em recuperação
'''
print('Bem vindo ao programa ' + titulo)

print('Por favor, informe a primeira nota')
nota_1 = float(input())

print('Informe a segunda nota')
nota_2 = float(input())

media = (nota_1 + nota_2) / 2

print('A média é %.2f' % media)

if media > 7:
    print('Aluno aprovado')
elif media < 5:
    print('Aluno reprovado')
else:
    print('Aluno em recuperação')