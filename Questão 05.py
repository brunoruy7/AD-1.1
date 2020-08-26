def regra1(n):
    a = n
    if n % 2 == 0:
        a = n / 2
    return a
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
    if n == 42:
        return True
    if regra1(n) != n:
        c += 1
    else:
        t1 = False
    if regra2(n) != n:
        c += 1
    else:
        t2 = False
    if regra3(n) != n:
        c += 1
    else:
        t3 = False
    for i in range (c):
        if regra1(n) != n and i == 0:
            a = regra1(n)
            t1 = jogobarra(a)
            if t1 == True:
                return True
        elif (regra2(n) != n or (t1 == False and regra2(n) != n)) and t2 != False :
            a = regra2(n)
            t2 = jogobarra(a)
            if t2 == True:
                return True
        elif (regra3(n) != n  or (t1 == False and regra3(n) != n) or (t2 == False and regra2(n) != n)) and t3 != False:
            a = regra3(n)
            t3 = jogobarra(a)
            if t3 == True:
                return True
    if t1 == t2 == t3 == False or n < 42:
        return False
n = int(input())
if jogobarra(n) == True:
    print('Venci')
else:
    print('Perdi')