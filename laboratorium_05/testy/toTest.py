'''
Na szachownicy o wymiarach 100 na 100 umieszczamy N skoczków (N<100). Położenie skoczków jest opisywane przez tablicę
 dane = [(w1, k1), (w2, k2), (w3, k3), ..., (wN, kN)]
Proszę napisać funkcję, która zwróci położenie skoczków wzajemnie się szachujących.
Do funkcji należy przekazać położenie skoczków. Należy zwizualizować rozkład skoczków na szachownicy.
'''
import random
#walidacja n
def checker(x):
    while not isinstance(x,int) or x<=0 or x>=100:
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int) and (x<=0 or x>=100):
            x = input('Podaj liczbe calkowita: ')
    return x

def ladnyPrint(tab):
    for i in tab:
        print(*i)
    print()

def mordkiSieSzachuja(dane):
    tabX=[2, 1, -1, -2, -2, -1, 1, 2] #wszystie mozliwe ruchy skoczka
    tabY=[1, 2, 2, 1, -1, -2, -2, -1]

    tabSkoczkow=[] #tablica zawierajaca skoczki wzajemnie sie szachujace

    tab=[['.' for _ in range(100)] for _ in range(100)]
    for i in dane:  tab[i[0]][i[1]]='S' #uzupelnienie tablicy skoczkami
    for x,y in dane:
        for i,j in zip(tabX,tabY):
            if 0<=x+i<100 and 0<=y+j<100:
                if tab[x+i][j+y]=='S':
                    if y+j>y and [(x+i,y+j),(x,y)] not in tabSkoczkow: tabSkoczkow.append([(x+i,y+j),(x,y)])
                    elif y+j<y and [(x,y),(x+i,y+j)] not in tabSkoczkow: tabSkoczkow.append([(x,y),(x+i,y+j)])
    ladnyPrint(tab)
    return tabSkoczkow

#n = checker(input('Ile ma byc skoczkow?\n'))
dane = [(random.randint(0,99), random.randint(0,99)) for _ in range(100)]

if __name__=='__main__':
    mordkiSieSzachuja(dane)