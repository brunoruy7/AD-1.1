def pad1(n):
    if n == 1:
        res1 = '#\n'
    else:
        res1 = pad1(n-1) + '#'*n + '\n'
    return res1
def pad2(n):
    if n == 1:
        print('#')
    else:
        for i in range(n):
            if i == 0:
                print(' '*n, '#')
            elif i == 1:
                print(' '*(n-i), '# #')
            else:
                print(' ' * (n - i), '#', ' ' * (1 + 2 * (i - 1)-2), '#')
        for i in range(n-2,-1,-1):
            if i == 0:
                print(' '*n, '#')
            elif i == 1:
                print(' '*(n-i), '# #')
            else:
                print(' '*(n-i), '#', ' '*(1+2*(i-1)-2), '#')
def pad3():
    r = ''
    r = (' ' * 5 + '_\n' + ' ' * 3 + '_( )_\n' + ' ' * 1 + '_|     _|\n' + ' ' * 0 + '(_   _ (_\n' + ' ' * 2 + '|_(  )_|')
    return r

print(pad3())
n = int(input())
print(pad1(n))
pad2(n)