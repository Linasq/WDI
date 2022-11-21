'''
Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n i wypełniający ją liczbami ciągu Fibonacciego po spirali.
Wymiar tablicy powinien być definiowany przez użytkownika.
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

#troche bardziej czytelnie printuje tablice
def ladnyPrint(tab):
    for i in tab:
        print(i)

#return tablicy z liczbami fib
def fib(x):
    n=x*x
    tab=[1,1]
    for i in range(1,n-1):
        tab.append(tab[i]+tab[i-1])
    return tab

#zwraca spirale w naszej tablicy
def spiralThing(x,tab):
    t=[[0 for _ in range(x)] for _ in range(x)]
    t[0][0]=1
    i,ii,ind=0,0,1
    while ind<x**2:
        while ii+1<x and t[i][ii+1]==0:
            t[i][ii+1]=tab[ind]
            ind+=1
            ii+=1
        while i+1<x and t[i+1][ii]==0:
            t[i+1][ii]=tab[ind]
            ind+=1
            i+=1
        while ii-1>=0 and t[i][ii-1]==0:
            t[i][ii-1]=tab[ind]
            ind+=1
            ii-=1
        while i-1>=0 and t[i-1][ii]==0:
            t[i-1][ii]=tab[ind]
            ind+=1
            i-=1
    return t

x=checker(input('>'))
tab=fib(x)
ladnyPrint(spiralThing(x,tab))