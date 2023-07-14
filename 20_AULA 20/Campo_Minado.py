import random, copy

largura = 10
altura = 10
bombas = 10

matrix_secreta = []

for x in range(largura):
    coluna = []
    for y in range(altura):
        coluna.append('.')
    matrix_secreta.append(coluna)

matrix_usuario = copy.deepcopy(matrix_secreta)

while bombas > 0:
    random_x = random.randint(0,9)
    random_y = random.randint(0,9)
    if matrix_secreta[random_y][random_x] != '#':
        matrix_secreta[random_y][random_x] = '#'
        bombas -= 1

print('CAMPO MINADO\n\n')
impressao_y = 'ABCDEFGHIJ'
while True:
    for x in range(largura):
        print(impressao_y[x], end='  ')
        for y in range(altura):
            print(matrix_usuario[y][x], end=' ')
        print()
    print('   1 2 3 4 5 6 7 8 9 10')

    try:
        escolha = input('Digite uma posição (ex: D5): ').upper()
        usuario_x = -999
        for indice, letra in enumerate(impressao_y):
            if letra == escolha[0]:
                usuario_x = indice


        usuario_y = int(escolha[1:]) - 1


        if matrix_secreta[usuario_y][usuario_x] == '#':
            print('Você explodiu')
            for x in range(largura):
                for y in range(altura):
                    print(matrix_secreta[y][x], end=' ')
                print()
            print('\n\n\n\n')
            break
        else:
            coord_esq = usuario_x - 1
            coord_dir = usuario_x + 1
            coord_sup = usuario_y - 1
            coord_inf = usuario_y + 1

            num_viz = 0

            if coord_esq >= 0:
                if coord_sup >= 0:
                    if matrix_secreta[coord_sup][coord_esq] == '#':
                        num_viz += 1
            if coord_sup >= 0:
                if matrix_secreta[coord_sup][usuario_x] == '#':
                    num_viz += 1
            if coord_dir < 10:
                if coord_sup >= 0:
                    if matrix_secreta[coord_sup][coord_dir] == '#':
                        num_viz += 1

            if coord_esq >= 0:
                if matrix_secreta[usuario_y][coord_esq] == '#':
                    num_viz += 1
            if coord_dir < 10:
                if matrix_secreta[usuario_y][coord_dir] == '#':
                    num_viz += 1

            if coord_esq >= 0:
                if coord_inf < 10:
                    if matrix_secreta[coord_inf][coord_esq] == '#':
                        num_viz += 1
            if coord_inf < 10:
                if matrix_secreta[coord_inf][usuario_x] == '#':
                    num_viz += 1
            if coord_dir < 10:
                if coord_inf < 10:
                    if matrix_secreta[coord_inf][coord_dir] == '#':
                        num_viz += 1

            matrix_usuario[usuario_y][usuario_x] = num_viz

            venceu = True
            for x in range(largura):
                for y in range(altura):
                    if matrix_usuario[y][x] == '.':
                        if matrix_secreta[y][x]  != '#':
                            venceu = False

            if venceu == True:
                print('Você venceu!!!')
                for x in range(largura):
                    for y in range(altura):
                        print(matrix_secreta[y][x], end=' ')
                    print()
                print('\n\n\n\n')
                break
    except:
        print('Você fez alguma coisa errada amigão')