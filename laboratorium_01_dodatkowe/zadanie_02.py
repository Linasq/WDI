'''
Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem:

A(n)=n∗n+n+1.

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
bl=True
for i in range(1,  int(x**0.5)+1):
    if x%(i*i+i+1)==0:
        print(f'Liczba {x} jest wielokrotnością dowolnego wyrazu ciągu danego wzorem: A(n)=n∗n+n+1 dla n={i}')
        bl=False
if bl:
    print(f'Liczba {x} nie jest wielokrotnością dowolnego wyrazu ciągu danego wzorem: A(n)=n∗n+n+1')