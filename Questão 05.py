def jogobarra(n):
    a = n
    k = 0
    if a > 42:
        if n % 2 == 0:
            a = n/2
        elif n % 3 == 0 or n % 4 == 0:
            a = n - (n%10) * ((n // 10) % 10)
        elif n % 5 == 0:
            a = n - 42
        else:
            k = 1
        if k != 1:
            jogobarra((a))
    if a == 42:
        res = True
    else:
        res= False
    return res
n = int(input())
if jogobarra(n) == True:
    print('Venci')
else:
    print('Perdi')
