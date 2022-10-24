'''
Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2,3,5.
Jedynka też jest taką liczbą.
Należy napisać program, który wylicza ile takich liczb znajduje się w przedziale od 1 do N włącznie,
gdzie N jest wczytywane.

Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną.
'''

x = input('Podaj liczbe: ')
while not isinstance(x,int) or x<0:
    try:
        x=int(x)
    except:
        x=input('Podaj liczbe calkowita: ')
    if isinstance(x,int) and x<0:
        x = input('Podaj liczbe calkowita: ')

def ileDzielnikow(n):
    tab235=[2,3,5]
    if n==1:
        return True
    else:
        for i in tab235:
            while n%i==0:
                n//=i
        if n>1: return False
        else: return True
z=0
for i in range(1,x+1):
    if ileDzielnikow(i):
        z+=1
print(z)