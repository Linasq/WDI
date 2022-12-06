'''
Rozwiąż rekurencyjnie Problem Skoczka Szachowego. Wskaż kolejne ruchy skoczka wypisując macierz.
'''
#by bylo ladnie widac tablice koncowa
def ladnyPrint(tab):
    for i in tab:
        print(*i)
    print()

#funkcja, w ktorej dzieje sie magia
def problem(tab,i, x=0,y=0):
    if i==65: exit(ladnyPrint(tab)) #8*8=64, wiec jak i bedzie mialo 65, to koniec

    tabX=[x+2, x+1, x-1, x-2, x-2, x-1, x+1, x+2] #wszystie mozliwe ruchy skoczka
    tabY=[y+1, y+2, y+2, y+1, y-1, y-2, y-2, y-1]

    for x1,y1 in zip(tabX,tabY):
        if 0<=x1<8 and 0<=y1<8:
            if tab[x1][y1]==0:
                tab[x1][y1] = i #nasz backtracking algorytm
                problem(tab, i+1, x1, y1)
                tab[x1][y1] = 0

tab=[[0 for _ in range(8)] for _ in range(8)] #lista wypelniona 0
tab[0][0]=1
problem(tab,2)

'''
znajduje to co ponizej, ale po 5 min
1 34 36 62 31 18 9 64
35 56 32 58 10 63 30 17
33 2 54 37 61 28 19 8
55 44 57 27 59 11 16 29
45 53 3 60 38 24 7 20
43 50 46 39 26 21 12 15
52 48 41 4 23 14 25 6
49 42 51 47 40 5 22 13
'''