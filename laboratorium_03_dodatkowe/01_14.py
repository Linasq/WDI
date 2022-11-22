'''
Mając wejściowy słownik, w którym klucze są dowolne (np. napisy) a wartościami są listy o różnej długości wypełnione liczbami,
posortuj słowniki według sumy liczb w tych listach.
Dodatkowo stwórz nowy słownik, w którym wartościami będą obliczone sumy.
Wejściowy słownik należy wygenerować korzystając z biblioteki random.
'''
import random

def ladnyPrint(n):
    for k,v in n.items():
        print(f'{k} : {v}')

dc={}
for i in range(10):
    n=random.randint(2,10)
    tab=[random.randint(0,100) for _ in range(n)]
    dc[i]=tab

print('slownik przed posortowaniem: \n')
ladnyPrint(dc)
print()
dc={k:v for k,v in sorted(dc.items(), key=lambda x: sum(x[1]))}

print('slownik po posortowaniu:\n')
ladnyPrint(dc)
print()
dcSum={k:sum(v) for k,v in dc.items()}
print("nowy slownik po obliczeniu sumy:\n")
ladnyPrint(dcSum)