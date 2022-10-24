'''
Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną.
'''
x=input('Podaj liczbe: ')
while not isinstance(x,int) or x<0:
    try:
        x=int(x)
    except:
        x=input('Podaj liczbe calkowita: ')
    if isinstance(x,int) and x<0:
        x = input('Podaj liczbe calkowita: ')

#tablica dzielnikow liczby x
tabD=[]
i=1
#petla wpisujace dzielniki do tablicy
while i<=int(x**0.5):
    if x%i==0:
        tabD.append(i)
    i+=1

#tablica liczb fib
tabF=[]
f1=1
f2=1
#petla dodajaca liczby fib do tabeli
while f2<=x:
    tabF.append(f2)
    f3=f1+f2
    f1,f2=f2,f3
z=0
for i in tabD:
    if i in tabF and x//i in tabF:
        print(f'Liczba {x} jest iloczynem tej pary z ciagu Fibonacciego: {i}, {x//i}')
        z+=1
if z==0:
    print('Twoja liczba nie jest iloczynem zadnej par wyrazow z ciagu Fibonacciego')