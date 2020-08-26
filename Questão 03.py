def matriz():
    a = input()
    menor = []
    maior = []
    matriz = ''
    c = 0
    while a != '':
        b = a.split()
        for i in range(len(b)):
            b[i] = float(b[i])
            if i == 0:
                maior.append(b[i])
                menor.append(b[i])
            elif b[i] > maior[c]:
                maior[c] = b[i]
            elif b[i] < menor[c]:
                menor[c] = b[i]
            matriz += '{:.2f} '.format(b[i])
        matriz += '\n'
        c += 1
        a = input()
    print(matriz)
    for j in range(len(menor)):
        print('Menor e Maior da Linha {}: {:.2f} e {:.2f}'.format(j+1,menor[j],maior[j]))
    maior = sorted(maior)
    menor = sorted(menor)
    print('Menor e Maior de Toda a Matriz: {:.2f} e {:.2f}'.format(menor[0], maior[len(maior)-1]))
matriz()