def matriz():
    menor = [] # Definindo variáveis para o programa.
    maior = []
    matriz = ''
    c = 0   # variável auxiliar para controlar qual linha da matriz estou lidando.
    while True:
        b = input().split()  # criado variável b string e usado o split para separar os números.
        if b == []:
            break # Saida do loop.
        for i in range(len(b)):
            b[i] = float(b[i]) # Convertendo os números de string para float.
            if i == 0: # Primeiro maior e menor de cada linha adicionado à respectiva lista.
                maior.append(b[i])
                menor.append(b[i])
            elif b[i] > maior[c]: # Comparado os valores com o maior/menor atual para deixar apenas o menor/maior de cada linha guardado nas listas.
                maior[c] = b[i]
            elif b[i] < menor[c]:
                menor[c] = b[i]
            matriz += '{:.2f} '.format(b[i])  # Aqui adiciona-se os valores à matriz a cada passada do for.
        matriz += '\n' # Trocando de linha da matriz.
        c += 1 # Contador da linha atualizado.
    print('Conteúdo da Matriz:')
    print(matriz)
    for j in range(len(menor)): # Como o maior/menor de cada linha ficou guardado na posição correspondente a linha, um for resolve nosso problema de distribuir adequadamente.
        print('Menor e Maior da Linha {}: {:.2f} e {:.2f}'.format(j+1, menor[j], maior[j]))
    print('Menor e Maior de Toda a Matriz: {:.2f} e {:.2f}'.format(min(menor), max(maior))) # Utilizado funções min e max nas listas menor/maior para achar o menor e maior de toda matriz.

matriz() # Chamada da função.