'''
Proszę napisać program wczytujący liczbę naturalną z klawiatury
i rozkładający ją na iloczyn 2 liczb o najmniejszej różnicy.
Przykład: 30=5∗6, 120=10∗12.

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

i=int(x**0.5)
while i!=0:
    if x%i==0:
        print(i,int(x/i))
        break
    i-=1