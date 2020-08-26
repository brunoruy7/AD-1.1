n = int(input())
contpar = 0
contimpr = 0
contprim = 0
maior = 0
medpar = 0
medimpr = 0
medprim = 0
if n <= 0:
    print('Nenhum número maior que zero foi lido!!!')
else:
    while n > 0:
        t = 0
        if n > maior:
            maior = n
        if n % 2 == 0:
            contpar += 1
            medpar += n
        else:
            contimpr += 1
            medimpr += n
        for i in range (2,n):
            if n % i ==0:
                t += 1
        if t == 0 and n != 1:
            contprim += 1
            medprim += n
        n = int(input())
    medpar = medpar/ contpar
    medprim = medprim/contprim
    medimpr = medimpr/contimpr
    print('Maior Número Lido: {}'.format(maior))
    print('Quantidade de Pares: {} com média: {:.2f}'.format(contpar,medpar))
    print('Quantidade de Ímpares: {} com média: {:.2f}'.format(contimpr,medimpr))
    print('Quantidade de Primos: {} com média: {:.2f}'.format(contprim,medprim))
