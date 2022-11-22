'''
Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n wypełnioną liczbami naturalnymi.
Dla danej tablicy należy napisać funkcję, która zwraca liczbę par elementów,
o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka szachowego.
Wymiar tablicy powinien być definiowany przez użytkownika.
'''
import random

#walidacja n
def checker(x):
    while not isinstance(x,int) or x<=0:
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int) and x<=0:
            x = input('Podaj liczbe calkowita: ')
    return x

#funkcja zwracajaca ilosc elementow, ktore w ruchu skoczka maja 2 czynnik taki, ze n1*n2=p
def chessGuy(t,p):
    n=len(t)
    cnt=0
    for y in range(n):
        for x in range(n):
            for x1,y1 in [(x+1,y+2),(x+1,y-2),(x+2, y+1),(x+2,y-1),(x-1,y+2),(x-1,y-2),(x-2, y+1),(x-2,y-1)]:
                if 0<=x1<n and 0<=y1<n:
                    if t[y][x]*t[y1][x1]==p:
                        #print(f'1. Wspolrzedne: [{x},{y}], wartosc: {t[y][x]}\n2. Wspolrzedne: [{x1},{y1}], wartosc: {t[y1][x1]}')
                        cnt+=1
    return cnt//2

n=checker(input('Wymiar: '))
p=checker(input('Iloczyn, ktory bedzie szukany: '))

t=[[random.randint(0,10) for _ in range(n)] for _ in range(n)]

print(chessGuy(t,p))