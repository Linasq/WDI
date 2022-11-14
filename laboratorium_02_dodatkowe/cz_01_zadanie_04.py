'''
Proszę napisać program wczytujący 3 liczby całkowite: N,M,L.
N to długość listy, M to granica górna zakresu a L jest granicą dolną zakresu.
Wykorzystując funkcję random.randint() należy wpisać do listy N losowych liczb całkowitych z zakresu M do L.
Należy znaleźć najdłuższy spójny podciąg rosnący, wypisać go i obliczyć sumę wszystkich elementów tego podciągu. Rozważ przypadki z ciągiem słabo i silnie rosnącym.
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

n = checker(input('Dlugosc listy: '))
m = checker(input('Gorna granica zakresu: '))
l = checker(input('Dolna granica zakresu: '))

while l>=m:
    m = checker(input('Gorna granica zakresu: '))
    l = checker(input('Dolna granica zakresu: '))

#tablica wypelniona losowymi liczbami wg zadania
tab=[random.randint(l,m) for _ in range(n)]

#zmienne dla podciagu silnie rosnacego
maxR=0
iR=0
cntR=1
#zmienne dla podciagu slabo rosnacego
maxr=0
ir=0
cntr=1

#petla znajdujaca obydwa te podciagi
for i in range(1, len(tab)):
    if tab[i-1]<tab[i]:
        cntR+=1
        if maxR < cntR:
            maxR = cntR
            iR = i+1
    else:
        cntR=1
    if tab[i-1]<=tab[i]:
        cntr+=1
        if maxr < cntr:
            maxr = cntr
            ir = i+1
    else:
        cntr=1

print(tab[iR-maxR:iR], sum(tab[iR-maxR:iR]))
print(tab[ir-maxr:ir], sum(tab[ir-maxr:ir]))