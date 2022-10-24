'''
Proszę napisać program, który wyznacza ostatnią niezerową cyfrę N!.
Program powinien działać dla N rzędu 1000000, gdzie N jest wczytywane z konsoli.

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

result=1
for i in range(1,x+1):
    while i%10==0:#obcinanie zer w i
        i//=10
    while result%10==0:#obcinanie zer w wyniku
        result//=10
    if result>1000000: #obcinianie poczatku, by program sie 'nie meczyl'
        result%=1000000
    result *= i
while result%10==0:
    result//=10
print(f'Ostatnia cyfra z {x}! wynosi: {result % 10}')