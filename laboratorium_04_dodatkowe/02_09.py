'''
Proszę napisać program wskazujący (rekurencyjnie) wszystkie możliwe podziały liczby naturalnej na sumę składników.
Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
'''
#walidacja n
def checker(x):
    while not isinstance(x,int) or x<=0:
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int) and x<=0:
            x = input('Podaj liczbe calkowita: ')
    return x

def splitSum(num, j, tab):
    if num == 0:
        for i in tab:
            if i==0:break
            print(i,end=' ')
        print()
        return

    if j == 0: mini=1
    else: mini=tab[j-1]

    for i in range(mini, num+1):
        tab[j]=i
        splitSum(num-i, j+1, tab)
        tab[j]=0

x=checker(input('> '))

splitSum(x, 0, [0 for i in range(x)])