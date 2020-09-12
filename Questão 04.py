def pad1(n): # Primeiro padrão
    if n == 1:
        res1 = '#\n'
    else:
        res1 = pad1(n-1) + '#'*n + '\n' # Recursão desenhando o número de # necessários em cada linha e indo para próxima.
    return res1  # poderia substituir esse return por um print(res1), fora do if/else para seguir a lógica dos outros padrões.
def pad2(n): # Segundo padrão
    if n == 1:
        print('#') # Caso em que o padrão é um único #.
    else:
        for i in range(n):
            if i == 0:
                print(' '*n, '#') # os ' '*n e afins antes da segunda parte do print é apenas para questão de alinhameto do desenho.
            elif i == 1:
                print(' '*(n-i), '# #')
            else:
                print(' ' * (n - i), '#', ' ' * (1 + 2 * (i - 1)-2), '#') # Adicionado fórmula para os espaçamentos internos, até a metade do desenho.
        for i in range(n-2,-1,-1): # Aqui é a segunda metade do desenho e, já que a lógica inverte, invertemos a ordem de progreção do desenho.
            if i == 0:
                print(' '*n, '#')
            elif i == 1:
                print(' '*(n-i), '# #')
            else:
                print(' '*(n-i), '#', ' '*(1+2*(i-1)-2), '#')
def pad3(n): # Terceiro padrão
    for k in range (n): # Adicionado loop para cada bloco de linhas (linha de peças).
        if k == 0:  # O padrão muda levemente de em cada tipo de bloco, esse é o primeiro.
            for i in range(n): # Aqui teremos um for para cada linha dos blocos com o end ='' para não mudar de linha de uma peça para outra do mesmo bloco de linha.
                print(' '*5 + '_ ', end= '') # Mesma lógica de multiplicar os espaços da questão anterior, dessa vez apenas para economizar linha.
            print('\n   ', end = '') # Mudando de linha
            for i in range(n):
                print('_( )__' + ' ',end = '')
                if i == n-1:
                    print('')
            for i in range (n+1):
                print(' ' + '_|' + ' '*4, end = '')
                if i == n:
                    print('')
            print('(_' + ' '*3, end = '')
            for i in range(n):
                print('_ ' + '(_ ', end = '  ')
                if i == n-1:
                    print('')
            print(' |', end = '')
            for i in range(n):
                print('__( )_', end= '|')
                if i == n-1:
                    print('')
        elif k % 2 != 0: # Aqui começam os blocos impares, que, como algumas partes se fundem com outras já desenhadas fica menor, fora isso a lógica é a mesma.
            for i in range(n):
                if i == 0:
                    print(' |_', end = '')
                print('     |_', end = '')
                if i == n -1:
                    print('')
            for i in range(n):
                if i == 0:
                    print('  _)', end = '')
                print(' _   _)', end = '')
                if i == n-1:
                    print('')
            for i in range (n):
                if i ==0:
                    print(' |', end = '')
                print('__( )_|', end='')
                if i == n-1:
                    print('')
        elif k % 2 == 0: # Aqui são os blocos pares, vale o mesmo citado para os impares
            for i in range (n+1):
                print(' ' + '_|' + ' '*4, end = '')
                if i == n:
                    print('')
            print('(_' + ' '*3, end = '')
            for i in range(n):
                print('_ ' + '(_ ', end = '  ')
                if i == n-1:
                    print('')
            print(' |', end = '')
            for i in range(n):
                print('__( )_', end= '|')
                if i == n-1:
                    print('')
n = int(input())
print(pad1(n)) # Chamando cada uma das funções, outra alternativa era criar uma função que chamasse as outras 3  para o usuário.
pad2(n)
pad3(n)