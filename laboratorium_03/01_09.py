'''
Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n wypełnioną liczbami naturalnymi.
Dla danej tablicy należy napisać funkcję, która zwraca wiersz i kolumnę dowolnego elementu,
dla którego iloraz sumy elementów w kolumnie w którym leży element do sumy elementów wiersza w którym leży element jest największa.
Wymiar tablicy powinien być definiowany przez użytkownika.
'''
import random

def ladnyPrint(tab):
    for i in tab:
        print(i)

#walidacja jak zawsze
def checker(x):
    while not isinstance(x,int) or x<=0:
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int) and x<=0:
            x = input('Podaj liczbe calkowita: ')
    return x

#funkcja zwraca x,y gdzie jest najwiekszy wynik dzielenia
def returnColRow(tab):
    n=len(tab)
    maxNum=0
    indX=0 #index x
    indY=0 #index y
    for i in range(n):
        for ii in range(n):
            sumWierszy=sum(tab[i]) #suma wierszy
            tabKol=[tab[x][ii] for x in range(n)] #lista zawierajaca liczby z danej kolumny
            sumKol=sum(tabKol) #suma z listy kolumn
            num=sumKol/sumWierszy #wynik dzielenia
            if num>maxNum:
                maxNum=num
                indX=ii
                indY=i
    print(maxNum)
    return f'x: {indX}\ny: {indY}'

n=checker(input('Wymiar tablicy 2D\n'))

tab=[[random.randint(1,10**17) for _ in range(n)]for _ in range(n)]
ladnyPrint(tab)
print(returnColRow(tab))

tabTest=[[i*j for i in range(1,11)] for j in range(1,11)]
ladnyPrint(tabTest)
print(returnColRow(tabTest))