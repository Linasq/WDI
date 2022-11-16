'''
Proszę napisać program wczytujący 3 liczby całkowite: N, M, L.
N to długość listy, M to granica górna zakresu a L jest granicą dolną zakresu.
Wykorzystując funkcję random.randint() należy wpisać do listy N losowych liczb całkowitych z zakresu M do L.
Należy znaleźć najdłuższy spójny podciąg arytmetyczny, wypisać go i obliczyć sumę wszystkich elementów tego podciągu. Oprócz liczb losowych należy przedstawić inne przykłady.
'''
import random

#walidacja liczb
def checker(x):
    while not isinstance(x,int) or x<=0:
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int) and x<0:
            x = input('Podaj liczbe calkowita: ')
    return x

#funkcja, ktora znajdzie i wypisze najdluzszy spojny podciag arytmetyczny, a nastepnie obliczy sume tego podciagu
def printAndCountSum(tab):
    tabr=[tab[i]-tab[i-1] for i in range(1, len(tab))]
    cnt=1
    ir=0
    maxCnt=0
    for i in range(1,len(tabr)):
        if tabr[i]==tabr[i-1]:
            cnt+=1
            if maxCnt<cnt:
                maxCnt=cnt
                ir=i
        else:
            cnt=1
    print(f'Najdluzszy podciag: {tab[ir-maxCnt+1:ir+2]}\nSuma elementow tego podciagu: {sum(tab[ir-maxCnt+1:ir+2])}')

n = checker(input('Dlugosc listy: '))
m = checker(input('Gorna granica zakresu: '))
l = checker(input('Dolna granica zakresu: '))

while m<=l:
    l=checker(input(f'Dolna granica musi byc mniejsza od {m}\nPodaj liczbe: '))

#tablice: 1 losowa i 2 testowe
tab=[random.randint(l,m) for _ in range(n)]
tab2=[2*i for i in range(10)]
tab3=[1,2,3,5,5,7,9,11,13,2]

printAndCountSum(tab)
printAndCountSum(tab2)
printAndCountSum(tab3)