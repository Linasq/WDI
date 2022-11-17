'''
Napisz program, który utworzy i wypisze listę składającą się z N liczb z przedziału [1,100]
a następnie po każdej liczbie pierwszej wstawi nowy element o wartości 0.
Następnie program powinien policzyć sumy podzbiorów znajdujących się pomiędzy zerami.
Lista przed modyfikacją: [7,45,45,34,53,45,4,3,11,18,30].
Lista po modyfikacji: [7,0,45,45,34,53,0,45,4,3,0,11,0,18,30].
Wynik: 7;177;52;11;48.
Wykorzystaj funkcje.
'''
import random

def isPrime(n):
    if n==2:
        return True
    elif n<2 or n%2==0:
        return False
    else:
        for i in range(3, int(n**0.5)+1,2):
            if n%i==0: return False
    return True

#walidacja liczby
x=input('Podaj dlugosc listy: ')
while not isinstance(x, int) or x <= 0:
    try:
        x = int(x)
    except:
        x = input('Podaj liczbe calkowita: ')
    if isinstance(x, int) and x < 0:
        x = input('Podaj liczbe calkowita: ')

#tablica na losowych n elementow oraz na sume przedzialow
tab=[random.randint(1,100) for _ in range(x)]
tabSum=[0]

#dodanie 0 do tablicy
for i in range(len(tab)+x):#taka dlugosc, bo nie wiemy ile 0 bedzie w tablicy
    if i >= len(tab): break #sprawdza, czy nie przesadzilismy z dlugoscia
    if isPrime(tab[i]):
        tab.insert(i + 1, 0)

#zliczanie przedzialow
n=0
for i in tab:
    if i!=0: tabSum[n]+=i
    else:
        if tab[-1]==0: break #pozbywamy sie 0 na koncu, jesli w tablicy jest to 0
        tabSum.append(0)
        n+=1

print(tab)
print(tabSum)