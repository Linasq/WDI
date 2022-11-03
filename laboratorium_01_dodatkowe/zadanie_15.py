'''
Mamy dane dwa ciągi o następujących zależnościach:

A:a0=0,a1=1,an=an−1−bn−1∗an−2
B:b0=2,bn=bn−1+2∗an-1

Proszę napisać program,
który czyta liczby typu 𝑖𝑛𝑡 ze standardowego wejścia i tak długo jak liczby te są kolejnymi wyrazami ciągu
An (tj. a0,a1,a2, …)
wypisuje na standardowe wyjście wyrazy drugiego ciągu Bn (tj. b0,b1,b2, …).

Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb całkowitych.
Należy obsłużyć wyjątek wczytania danej niebędącej liczbą całkowitą.
'''

def gimme():
    x = input('Podaj liczbe: ')
    while not isinstance(x,int):
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int):
            return x



a0=0
a1=1
b0=2
b1=2
n=2
bn=b0+2*a1
an=a1-b0*a0
while True:
    print(f'n: {n}')
    x = gimme()
    if x!=an:
        break
    else:
        print(bn)
        bn=b1+2*a1
        a0, a1, an= a1, an, a1 - b1 * a0
        b1=bn
    n+=1
