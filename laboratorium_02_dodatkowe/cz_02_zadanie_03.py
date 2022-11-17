'''
Proszę napisać program, który wypełnia N-elementową listę pseudolosowymi liczbami nieparzystymi z zakresu [1,99]
a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego znajdującego się w niej ciągu arytmetycznego o dodatniej różnic,
a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy,
przy założeniu, że kolejnymi wyrazami ciągu są elementy listy o kolejnych indeksach.
Należy także przygotować własne przypadki testowe.
Wykorzystaj funkcje, N jest podawane przez użytkownika.
'''
import random

def finder(tabR):
    cntP=2
    cntM=2
    maxP=2
    maxM=2
    for i in range(1,len(tabR)):
        if tabR[i]==tabR[i-1]:
            if tabR[i]>0:
                cntP+=1
                cntM=2
                if cntP>maxP: maxP=cntP
            elif tabR[i]<0:
                cntM+=1
                cntP=2
                if cntM>maxM: maxM=cntM
        else: cntP,cntM=2,2
    return maxP-maxM

#walidacja liczby
x=input('Podaj dlugosc listy: ')
while not isinstance(x, int) or x <= 0:
    try:
        x = int(x)
    except:
        x = input('Podaj liczbe calkowita: ')
    if isinstance(x, int) and x < 0:
        x = input('Podaj liczbe calkowita: ')

tabTest=[1,1,3,5,7,9,7,5,3]
tabTestR=[tabTest[i+1]-tabTest[i] for i in range(len(tabTest)-1)]

tabTest2=[1,3,33,3,5,7,9,7,7,5,11,33,99,77,55,33,11]
tabTestR2=[tabTest2[i+1]-tabTest2[i] for i in range(len(tabTest2)-1)]

tab=[random.randint(0,49)*2+1 for _ in range(x)]
tabR=[tab[i+1]-tab[i] for i in range(x-1)]

'''print(tabTest)
print(tabTestR)
print(finder(tabTestR))'''

print(tab)
print(tabR)
print(finder(tabR))

'''print(tabTest2)
print(tabTestR2)
print(finder(tabTestR2))'''