def relacao(n):
    n = n.split()
    if len(n) == 0:
        print('Nenhum Número Foi Lido!!!')
    else:
        print('Relação de Par(es):')
        for i in range(len(n)):
            n[i] = int(n[i])
            if n[i] % 2 == 0:
                print(n[i])
        print('Fim da Relação de Par(es).\n')
        print('Relação de Primo(s):')
        for j in range(len(n)):
            c = 0
            for k in range(2,n[j]):
                if n[j] % k == 0:
                    c += 1
            if c == 0 and n[j] > 1:
                print(n[j])
        print('Fim da Relação de Primo(s).')
n = input()
relacao(n)
