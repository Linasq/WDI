'''
Proszę napisać program, który łączy dwie listy dowolnej długości w słowniki, w dwóch trybach.
W pierwszym odpowiadające sobie elementy listy (po indeksach) tworzą parę klucz-wartość słownika
(wszystkie elementy jednej listy to klucze, a wszystkie elementy drugiej to wartości).
W drugim trybie poszczególne elementy jednej listy mogą być kluczem albo wartością
(wtedy odpowiadające elementy drugiej listy to wartości albo klucze) – należy skorzystać z biblioteki random.
Ponadto program powinien umożliwić zamianę odwrotną ze słownika na listy.
Należy obsłużyć wyjątek, w którym wprowadzone przez użytkownika listy nie mają równej długości.
'''
import random
import time

def checker(tab):
    while len(tab)<=1:
        tab=input('Tablica powinna miec wiecej niz 1 element:\n')
    return tab

#kazdy element listy 1 jest kluczem, a wartoscia jest odpowiedni el. listy 2
def tryb1(tab1,tab2):
    dc={k:v for k,v in zip(tab1,tab2)}
    return dc

#losowo albo el. listy 1 albo el. listy 2 jest kluczem, wtedy drugi el. jest wartoscia
def tryb2(tab1, tab2):
    dc={}
    for x,y in zip(tab1,tab2):
        k = random.choice([x,y])
        v= x if k!=x else y
        dc[k]=v
    return dc

#zamiana z slownika na listy
def zamiana(dc):
    tab1=[]
    tab2=[]
    for k,v in dc.items():
        tab1.append(k)
        tab2.append(v)
    return tab1, tab2

t1=checker(input('Podaj elementy do listy 1:\n').split())
t2=checker(input('Podaj elementy do listy 2:\n').split())

while len(t1)!=len(t2): t2=checker(input(f'Druga lista powinna miec {len(t1)} elementow\n').split())

dc={}
while True:
    x=input('Co chcesz zrobic?\n0. Exit\n1. Tryb 1\n2. Tryb 2\n3. Zamiana\n>')
    if x=='0':
        print('Do widzenia')
        quit()
    elif x=='1':
        dc=tryb1(t1,t2)
        print(dc)
        time.sleep(1)
    elif x=='2':
        dc=tryb2(t1,t2)
        print(dc)
        time.sleep(1)
    elif x=='3':
        if len(dc)<len(t1): print('Jeszcze nie masz slownika')
        else:
            t1,t2=zamiana(dc)
            print(f'Lista nr 1: {t1}\nLista nr 2: {t2}')
            time.sleep(1)
    else:
        print('Nie wiem co to jest')
        quit()