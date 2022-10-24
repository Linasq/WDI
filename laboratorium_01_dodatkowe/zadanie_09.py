'''
Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego,
np. 9, 14, 15, 17, 22. Proszę napisać program, który wczytuje liczbę naturalną n,
wylicza i wypisuje następną taką liczbę większą od n. Można założyć, że 0<n<1000.

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

#!!UWAGA!!
#ten program wypisuje nastepna liczbe wieksza od n i bedaca suma podciagu Fib

#suma i zmienna pamietajaca ostatnia zapamietana sume
rs, s=0,2
#4 zmienne, dzieki ktorym bede sie poruszac po ciagu Fib
low,slow = 1,1
high,shigh = 1,1
k=0
while True:
    if s<x:
        shigh,high=high,shigh+high
        s+=high
    elif s>x:
        rs=s
        s-=low
        low,slow=slow,low+slow
        k=1
    if s<x and k==1:
        print(f'To jest suma troche wieksza od tego co podales: {rs}, poniewaz nie ma takiego podciagu')
        break
    elif s==x:
        print(f'Istnieje podciag Fib, ktorego suma wynosi: {s}')
        break