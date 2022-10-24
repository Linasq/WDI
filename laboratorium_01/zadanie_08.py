import random

x = int(input('> '))

while x==0:
    x=int(input('> '))

x = -1*x if x<0 else x
i=0
spacja=x-1
while i<=x:
    if i==x:
        print(' '*(x-1)+'U')
    elif i==0:
        print(' '*spacja+'X')
        spacja-=1
    else:
        print(' '*spacja, end='')
        ileX = 2*i+1
        tab=['*' for i in range(ileX)]
        n=random.randint(0, ileX-1)
        tab[n]='o'
        powies=''.join(tab)
        print(powies)
        spacja-=1
    i+=1