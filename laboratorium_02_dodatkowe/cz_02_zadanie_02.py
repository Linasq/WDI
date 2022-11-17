'''
Dana jest N-elementowa lista zawierająca liczby naturalne.
W liście możemy przeskoczyć z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby lista[k].
Należy napisać funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola listy na ostatnie pole.
Należy rozważyć wszystkie przypadki.
'''
import random

#tworzymy nowa liste 0 i 1, jesli dana liczba jest podzielna przez czynnik pierwszy to t2[i+czynik]=1 i jesli przejedziemy przez wszystkie liczby i na samym koncu bedzie 1, to zwracamy prawde
def function(tab):
    n=len(tab)
    t2=[False for _ in range(n)]
    t2[0]=True
    for i in range(n):
        if t2[i]:
            temp=tab[i]
            k=2
            while temp!=1 and k<n:
               while temp%k==0:
                    if i+k<n: t2[i+k]=True
                    temp//=k
               k+=1
    return t2[-1]

#walidacja liczby
x=input('Podaj dlugosc listy: ')
while not isinstance(x, int) or x <= 0:
    try:
        x = int(x)
    except:
        x = input('Podaj liczbe calkowita: ')
    if isinstance(x, int) and x < 0:
        x = input('Podaj liczbe calkowita: ')

tab=[random.randint(1,10**10) for _ in range(x)]

print(function(tab))