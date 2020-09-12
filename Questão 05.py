def regra1(n): # Criado regras 1,2 e 3.
    a = n
    if n % 2 == 0:
        a = n / 2
    return a # retornado o próprio n, caso não satisfaça a condição ou satisfaça mas retorne o mesmo valor (Loop infinito).
def regra2(n):
    a = n
    if n % 3 == 0 or n % 4 == 0:
        a = n - (n % 10) * ((n // 10) % 10)
    return a
def regra3(n):
    a = n
    if n % 5 == 0:
        a = n - 42
    return a
def jogobarra(n):
    c = 0
    t1 = t2 = t3 = True
    if n == 42: # Saída vencedora.
        return True
    if regra1(n) != n: # Esse primeiro bloco de if's/else's verificam em quantas regras o número se encaixa, e quais são.
        c += 1
    else:
        t1 = False # caso não entre na respectiva regra, ou entre e retorne o mesmo valor ( cria um ciclo infinito) retorna falso para respectiva regra.
    if regra2(n) != n:
        c += 1
    else:
        t2 = False
    if regra3(n) != n:
        c += 1
    else:
        t3 = False
    for i in range (c): #Para cada regra em que se enquadre ele fará uma passagem.
        if regra1(n) != n and i == 0: # Só fará a regra 1 caso se enquadre na regra e seja a primeira passagem(caso não tenha testado essa hipótese antes).
            a = regra1(n)
            t1 = jogobarra(a) # Aqui testa-se novamente as regras para caso esse ramo cause um True no final.
            if t1 == True:
                return True # t1 recebeu jogobarra, se retornar True, significa que, utilizando esse ramo, chegou-se no final em um resultado vencedor, assim, retorna-se True.
        elif (regra2(n) != n or (t1 == False and regra2(n) != n)) and t2 != False : # Testa-se a regra 2 nos casos descritos, caso já tenha sido passado esse ramo, (c=3 por exmplo) t2 já terá sido atualizado para False.
            a = regra2(n)
            t2 = jogobarra(a)
            if t2 == True: # Mesma lógica da regra anterior.
                return True
        elif (regra3(n) != n  or (t1 == False and regra3(n) != n) or (t2 == False and regra2(n) != n)) and t3 != False: # Mesma lógica da regra 2, ajustado para a uma posição inferior de um elif.
            a = regra3(n)
            t3 = jogobarra(a) # Mesma lógica, caso este valor retorne False esse ramo foi testado e falhou e caso retorne True, obteve sucesso.
            if t3 == True:
                return True
    if t1 == t2 == t3 == False or n < 42: # Caso, todas as regras tenham sido testada, para todos os números, ou o inicial seja menor que 42, a saida final é False.
        return False
n = int(input())
if jogobarra(n) == True: # Chamada da função conforme solicitado.
    print('Venci')
else:
    print('Perdi')