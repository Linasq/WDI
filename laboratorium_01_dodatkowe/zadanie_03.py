'''
Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

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

#beda 2 sposoby, pierwszy to dzialanie na integerze, drugi to dzialanie na stringu
xPrim=0
temp=x
while temp!=0:
    xPrim*=10
    xPrim+=temp%10
    temp//=10

if x==xPrim:
    print(f'Liczba {x} jest palindromem')
else:
    print(f'Liczba {x} nie jest palindromem')

binX=0
xPrim=x
while x!=0:
    binX*=10
    binX+=x%2
    x//=2
if str(binX)==str(binX)[::-1]:
    print(f'Liczba {str(binX)[::-1]} jest palindromem')
else:
    print(f'Liczba {str(binX)[::-1]} nie jest palindromem')