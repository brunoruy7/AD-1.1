def relacao(n):
    n = n.split() # Criando a lista, ainda em formato de string.
    if len(n) == 0:
        print('Nenhum Número Foi Lido!!!') # checagem se foi digitado algo.
    else:
        print('Relação de Par(es):')
        for i in range(len(n)):
            n[i] = int(n[i]) #conversão de string para inteiro.
            if n[i] % 2 == 0: # Verificação de números pares.
                print(n[i])
        print('Fim da Relação de Par(es).\n') # adicionado o \n para o layaut do output ficar como demostrado nos exemplos, pulando uma linha.
        print('Relação de Primo(s):')
        for j in range(len(n)):
            c = 0  # variável auxiliar, para verificação de primos.
            for k in range(2,n[j]):
                if n[j] % k == 0:
                    c += 1
            if c == 0 and n[j] > 1:
                print(n[j])
        print('Fim da Relação de Primo(s).')
n = input()
relacao(n)  # Chamada da função