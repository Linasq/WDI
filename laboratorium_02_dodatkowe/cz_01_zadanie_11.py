'''
Wykorzystując odwzorowanie list (ang. list comprehension),
proszę porównać ze sobą kolejne elementy dwóch wcześniej wygenerowanych list (N, M, L jak w poprzednich zadaniach).
Jeśli elementy są równe do nowej listy należy wpisać True, w przeciwnym wypadku False.
Na koniec należy wybrać elementy o wartości False z jednej z początkowych list ponownie korzystając z mechanizmu odwzorowania list.
Dla porównania można skorzystać z metody itertools.compress().
'''
import random

#walidacja liczb
def checker(x):
    while not isinstance(x,int) or x<=0:
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int) and x<=0:
            x = input('Podaj liczbe calkowita: ')
    return x

n = checker(input('Dlugosc listy: '))
m = checker(input('Gorna granica zakresu: '))
l = checker(input('Dolna granica zakresu: '))

while m<=l: l=checker(input(f'Dolna granica musi byc mniejsza od {m}\nPodaj liczbe: '))

tab1=[random.randint(l,m) for _ in range(n)]
tab2=[random.randint(l,m) for _ in range(n)]

tabBool=[True if x==y else False for x,y in zip(tab1,tab2)]
tabFalse=[i for i,z in zip(tab1,tabBool) if not z]

print(len(tabFalse) ,tabFalse)