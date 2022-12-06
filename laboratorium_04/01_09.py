'''
Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury:
dane = [(x1, y1), ( x2, y2), (x3, y3), ..., (xN, yN)]
Proszę napisać funkcję, która zwraca wartość True, jeżeli w zbiorze istnieją 3
punkty wyznaczające trójkąt prostokątny o bokach przyprostokątnych równoległych do osi układu kartezjańskiego oraz wewnątrz którego nie ma żadnych innych punktów.
Do funkcji należy przekazać strukturę opisującą położenie punktów.
'''
import matplotlib.pyplot as plt
import random

#funckja obliczajaca odleglosc punktu od (0,0)
def howClose(tab):
#nie ma potrzeby pierwiastkowania, bo pierwiastek jest rowny wtw gdy liczba przed pierwiastkowaniem jest rowna
    for i in range(3): #przesuniecie, dalem w petli dla pewnosci, ale 3 iteracja juz raczej nic nie robi
        if tab[0][0]**2 + tab[0][1]**2 > tab[1][0] ** 2 + tab[1][1] ** 2: tab[0],tab[1]=tab[1],tab[0]
        if tab[1][0] ** 2 + tab[1][1] ** 2 > tab[2][0] ** 2 + tab[2][1] ** 2: tab[1],tab[2]=tab[2],tab[1]
    return tab

#znalezienie punktow, ktore by nam popsuly zadanie
def area(triangle,p):
    x1, y1 = triangle[0][0], triangle[0][1]#rozdzielenie kazdej wspolrzednej
    x2, y2 = triangle[1][0], triangle[1][1]
    x3, y3 = triangle[2][0], triangle[2][1]
    px, py = p[0], p[1]

    mainArea=(abs((x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)))/2 #obliczenie wszystkich pol
    area12p=(abs((x2-x1)*(py-y1)-(px-x1)*(y2-y1)))/2
    area13p=(abs((px-x1)*(y3-y1)-(x3-x1)*(py-y1)))/2
    area23p=(abs((x2-px)*(y3-py)-(x3-px)*(y2-py)))/2

    if mainArea==area23p+area12p+area13p: return True
    return False

#funkcja w ktorej sie wszystko dzieje
def trojkatProstokatny(dane):
    n=len(dane)
    tab=[] #tablica na wszystkie nasze trojkaty prostokatne

    for i in range(n-2):
        x=dane[i][0]#tworzenie pierwszej wspolrzednej
        y=dane[i][1]

        for ii in range(i,n):
            xx=dane[ii][0] #tworzenie drugiej wsp
            yy=dane[ii][1]
            if x==xx and y!=yy:
                 for iii in range(n):#wspolrzedne x, xx itd to sa wspolrzedne punktow, na ktorych sprawdzamy, czy mozna na nich opisac trojkat prostokatny
                     xxx=dane[iii][0]
                     yyy=dane[iii][1]

                     if xxx!=x and (y==yyy or yy==yyy):
                         triangle=howClose([(x,y),(xx,yy),(xxx,yyy)])
                         cnt = 0
                         for j in dane:
                            if area(triangle, j) and j not in triangle: #sprawdzamy czy dany punkt jest w trojkacie i zarazem nie jest 1 z wierzcholkow
                                cnt+=1
                         if triangle not in tab and cnt==0: tab.append(triangle)

            elif x!=xx and y==yy:
                for iii in range(n):
                    xxx = dane[iii][0]
                    yyy = dane[iii][1]
                    if yyy!=y and (x==xxx or xx==xxx):
                        triangle = howClose([(x, y), (xx, yy), (xxx, yyy)]) #od tego momentu leca powtorki, ale chory czlowiek nie mysli
                        cnt = 0
                        for j in dane:
                            if area(triangle,j) and j not in triangle:#sprawdzamy czy dany punkt jest w trojkacie i zarazem nie jest 1 z wierzcholkow
                                cnt+=1
                        if triangle not in tab and cnt==0: tab.append(triangle)

    x = [x[0] for x in dane] #przedstawienie wszystkich punktow na wykresie
    y = [y[1] for y in dane]
    plt.scatter(x, y, color='blue')

    x1,y1=[],[]
    for i in tab: #przedstawienie tylko punktow, ktore t
        for j in i:
            x1.append(j[0])
            y1.append(j[1])
    plt.scatter(x1,y1, color='red')
    plt.title('Punkty tworzace trojkat prostokatny')
    plt.show()

dane=[(random.randint(-100,100),random.randint(-100,100)) for _ in range(100)]  #dane randomowe
trojkatProstokatny(dane)

daneTest=[(2,10), (1,5), (2,-5), (10,10), (12,5), (-3,-7), (-3,-9)] #dane testowe
trojkatProstokatny(daneTest)