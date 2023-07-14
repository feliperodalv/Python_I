import random
import copy
import time

altura = 10
largura = 10

matrix = []

for x in range(largura):
    coluna = []
    for y in range(altura):
        vivo_morto = random.randint(0,1)
        if vivo_morto == 0:
            coluna.append('.')
        else:
            coluna.append('#')
    matrix.append(coluna)

matrix_nova = copy.deepcopy(matrix)

while True:
    matrix = copy.deepcopy(matrix_nova)
    print('\n' + '-'*40 + '\n')
    for x in range(largura):
        for y in range(altura):
            print(matrix[y][x],end='')
        print()


    for x in range(largura):
        for y in range(altura):
            coord_esq = x - 1
            coord_dir = x + 1
            coord_sup = y - 1
            coord_inf = y + 1

            num_viz = 0

            if coord_esq >= 0:
                if coord_sup >= 0:
                    if matrix[coord_sup][coord_esq] == '#':
                        num_viz += 1
            if coord_sup >= 0:
                if matrix[coord_sup][x] == '#':
                    num_viz += 1
            if coord_dir < 10:
                if coord_sup >= 0:
                    if matrix[coord_sup][coord_dir] == '#':
                        num_viz += 1

            if coord_esq >= 0:
                if matrix[y][coord_esq] == '#':
                    num_viz += 1
            if coord_dir < 10:
                if matrix[y][coord_dir] == '#':
                    num_viz += 1

            if coord_esq >= 0:
                if coord_inf < 10:
                    if matrix[coord_inf][coord_esq] == '#':
                        num_viz += 1
            if coord_inf < 10:
                if matrix[coord_inf][x] == '#':
                    num_viz += 1
            if coord_dir < 10:
                if coord_inf < 10:
                    if matrix[coord_inf][coord_dir] == '#':
                        num_viz += 1


            if matrix[y][x] == '#' and (num_viz == 2 or num_viz == 3):
                matrix_nova[y][x] = '#'
            elif matrix[y][x] == '.' and num_viz == 3:
                matrix_nova[y][x] = '#'
            elif matrix[y][x] == '#' and num_viz > 3:
                matrix_nova[y][x] = '.'
            elif matrix[y][x] == '#' and num_viz < 2:
                matrix_nova[y][x] = '.'

    time.sleep(1)