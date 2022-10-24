'''
Proszę napisać program wczytujący trzy liczby naturalne a,b,n
i wypisujący rozwinięcie dziesiętne ułamka (a/b) z dokładnością do n miejsc po kropce dziesiętnej (n jest rzędu 100).

Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną.
'''

def checker(n):
    x = input(f'Podaj {n}: ')
    while not isinstance(x,int) or x<0:
        try:
            x=int(x)
        except:
            x=input(f'Podaj liczbe calkowita {n}: ')
        if isinstance(x,int) and x<0:
            x = input(f'Podaj liczbe calkowita {n}: ')
    return x

a=checker('a')
b=checker('b')
n=checker('n')

print(f'{a // b}.',end='')
a=(a%b)*10
if a<b:
    print(0,end='')
for i in range(n):
    if a<b:
        a*=10
    if a>=b:
        print(a//b,end='')
        a=a%b
    else:
        print(0,end='')