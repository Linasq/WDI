'''
Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera.
Ile różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie?
Przykład: dla 2315 będą to 21, 35, 231, 315.

Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną
'''
x = input('Podaj liczbe: ')
while not isinstance(x,int) or x<0:
    try:
        x=int(x)
    except:
        x=input('Podaj liczbe calkowita: ')
    if isinstance(x,int) and x<0:
        x = input('Podaj liczbe calkowita: ')

def czyRozneCyfry(n):
    tab=[]
    while n>0:
        tab.append(n%10)
        n//=10
    if 0 in set(tab):
        return False
    elif len(set(tab))==len(tab):
        return True
    else:
        return False

def dlugosc(n):
    s=0
    while n>0:
        s+=1
        n//=10
    return s

#funkcja decBin zwraca nam liczbe binarna (np. 101) zamieniona na liczbe z cyframi z tabeli
def decBin(n,tab):
    z=0
    i=0
    while n!=0:
       if z%10!=0:
           z*=10
       if n%2==1:
           z+=tab[i]
       n//=2
       i+=1
    return z

def wszystkieKombinacje(dl,n):
    tab=[]
    i=dl
    #umieszczenie wszystkich cyfr w tabeli
    while i>0:
        tab.append(n//(10**(i-1)))
        n%=10**(i-1)
        i-=1
    for i in range(1,(2**dl)-1):
        bini=decBin(i,tab)
        if bini%7==0:
            print(bini)
    return

if czyRozneCyfry(x):
    dl=dlugosc(x)
    wszystkieKombinacje(dl,x)
else:
    print('Liczba nie spelnia wymagan!!')