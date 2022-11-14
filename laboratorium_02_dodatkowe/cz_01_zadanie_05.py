'''
Proszę napisać program,
który wypełnia listę tysiącem losowych liczb z dowolnego wskazanego zakresu przez użytkownika i sprawdzający,
czy w tym zakresie jest liczba zawierająca wyłącznie cyfry nieparzyste.
W celu generowania liczb można wykorzystać funkcję random.randint().
Należy wypisać wszystkie takie znalezione liczby w kolejności malejącej i obsłużyć wyjątek, w którym użytkownik podaje na wejściu liczby, które są równe.
'''
import random

#funkcja sprawdzajaca czy liczba zawiera same nieparzyste cyfry
def isOdd(n):
    while n!=0:
        x=n%10
        if x%2==0:
            return False
        n//=10
    return True

#walidacja liczb
def checker(x):
    while not isinstance(x,int):
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
    return x

m = checker(input('Gorna granica zakresu: '))
l = checker(input('Dolna granica zakresu: '))

#wypisanie tablicy 1000 losowych liczb
if m>l: tab=[random.randint(l,m) for _ in range(1000)]
else: tab=[random.randint(m,l) for _ in range(1000)]

#znalezienie wszystkich liczb spelniajacych warunek i wypisanie ich w kolejnosci posortowanej
tabOdd=[]
for i in tab:
    if isOdd(i): tabOdd.append(i)
print(sorted(tabOdd)[::-1])