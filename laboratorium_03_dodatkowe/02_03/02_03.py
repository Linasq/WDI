'''
Wykorzystując funkcje, napisz program tworzący plansze do sudoku (a przynajmniej w miarę).
Plansze należy następnie zapisać do osobnych plików.
Należy zapisać je w takiej formie, żeby były czytelne dla ludzkiego oka.
Ponadto trzeba obsłużyć niezbędne wyjątki.

x y z | z y x | z x c
1 2 3 | 1 2 3 | 2 2 2
4 4 4 | 4 4 4 | 4 4 4
- - - + - - - + - - -
x y z | z y x | z x c
1 2 3 | 1 2 3 | 2 2 2
4 4 4 | 4 4 4 | 4 4 4
- - - + - - - + - - -
x y z | z y x | z x c
1 2 3 | 1 2 3 | 2 2 2
4 4 4 | 4 4 4 | 4 4 4


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

#printuje do pliku czytelna plansze
def ladnyPrint(tab):
    x,y=0,0
    BIIGtab=[[' ' for _ in range(21)] for _ in range(11)]
    for a in range(11):
        for b in range(21):
            if a%4==3:
                if b==6 or b==14: BIIGtab[a][b]='+'
                else: BIIGtab[a][b]='-'
            else:
                if b==6 or b==14: BIIGtab[a][b]='|'
                elif b%2==0:
                    BIIGtab[a][b]=tab[y][x]
                    if x<8: x+=1
                    else:
                        x=0
                        y+=1
    with open('plansza.txt', 'w') as f:
        for i in BIIGtab:
            z=''
            for ii in i:
                z+=str(ii)
            z+='\n'
            f.writelines(z)
    print('Wygenerowano plansze! Plansza znajduje sie w pliku "plansza.txt"')


#zwraca tablice liczb, ktorych nie ma obrebie "sudoku"
def isIn(tab, x, y):
    mainTab=[]#tabela, laczaca wszystkie inne tabele

    tRows=tab[y]#liczby w wierszu
    mainTab.extend(tRows)

    tCols=[tab[i][x] for i in range(9)] #liczby w kolumnie
    mainTab.extend(tCols)

    modX=(x//3)*3#liczby w kwadracie 3x3
    modY=(y//3)*3
    tSquare=[[tab[i][ii] for ii in range(modX, modX+3)] for i in range(modY, modY+3)]

    for i in tSquare:
        mainTab.extend(i)

    mainTab=set(mainTab)#usuniecie duplikatow z tabeli
    tabReszta=[i for i in range(1,10) if i not in mainTab] #dodanie liczb, ktorych nie ma do tablicy

    return tabReszta

#tworzenie calej planszy
def createBoard():
    tab=[[" " for i in range(9)] for ii in range(9)]
    x,y=0,0
    while y < 9:
        x=0
        if y==9: break
        while x < 9:
            if x==0 and y==0: #dodanie pierwszej liczby do tablicy
                n = random.randint(1, 9)
                tab[y][x] = n
                x+=1
            else:
                tabReszt=isIn(tab,x,y)#tablica reszt zawiera liczby, ktore jescze nie zostaly uzyte
                if len(tabReszt)>0:
                    n = random.choice(tabReszt)
                    tab[y][x]=n
                    if x<8:x+=1
                    else:
                        y+=1
                        x=0
                    if y==9: break
                else:
                    x=0
                    y=0
                    tab=[[' ' for i in range(9)] for ii in range(9)]

    return tab

#usuniecie odpowiedniej ilosci elementow, w zaleznosci od n
def delNum(n, tab):
    tabBool=[0 for _ in range(n)]
    tabBool.extend([1 for _ in range(81-n)])
    random.shuffle(tabBool)
    i=0
    for y in range(9):
        for x in range(9):
            if not tabBool[i]:
                tab[y][x]=' '
            i+=1

    return tab

#funkcja rozruchowa
def main():
    print('+-----Generator plansz Sudoku-----+')
    print('+---------------------------------+')
    print('+-----Wybierz poziom trudnosci----+\n')
    n=checker(input(f'{" "*9}1. Poziom Latwy\n{" "*9}2. Poziom Sredni\n{" "*9}3. Poziom Trudny\n'))
    tab=createBoard()
    if n==1: tab=delNum(45,tab)
    elif n==2: tab=delNum(51, tab)
    elif n==3: tab=delNum(57, tab)
    else:
        print('To zes podal numer')
        quit()

    ladnyPrint(tab)

main()