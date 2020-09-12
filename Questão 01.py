#Apenas iniciando as variáveis necessárias para o código#
contpar = 0
contimpr = 0
contprim = 0
maior = 0
medpar = 0
medimpr = 0
medprim = 0
while True:
    n = int(input())
    t = 0  # Variável auxiliar para achar os números primos, declarada aqui para poder zerar acada número.#
    if n <= 0:
        if maior == 0:  # se o maior está igual à zero, significa que o número menor ou igual que zero foi o primeiro, já que qualquer outro teria substituido o maior.#
            print('Nenhum número maior que zero foi lido!!!')
        break # saida do loop#
    if n > maior:
        maior = n
    if n % 2 == 0:
        contpar += 1 # Como não sei quantos números seram lidos adicionei essa contagem para saber por quanto dividir a soma para achar a média.#
        medpar += n  # Preferi economizar uma variável e colocar a soma todal, nesse caso dos pares, aqui e, no final, dividir e acertar o valor.#
    else:
        contimpr += 1  # Mesmo funcionamento dos pares, os ptimos também tem a mesma lógica.#
        medimpr += n
    for i in range (2,n):
        if n % i == 0:
            t += 1
    if t == 0 and n != 1:
        contprim += 1
        medprim += n
# Acertando os valores das médias e dicionando os condicionáis para evitar erro de divizão por 0 caso usuário não digite nenhum de algum dos tipos de valores#
if contpar != 0:
    medpar = medpar/ contpar
if contprim != 0:
    medprim = medprim/contprim
if contimpr != 0:
    medimpr = medimpr/contimpr
print('Maior Número Lido: {}'.format(maior))
print('Quantidade de Pares: {} com média: {:.2f}'.format(contpar,medpar))
print('Quantidade de Ímpares: {} com média: {:.2f}'.format(contimpr,medimpr))
print('Quantidade de Primos: {} com média: {:.2f}'.format(contprim,medprim))