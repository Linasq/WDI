'''
Proszę napisać program,
który wypełnia N-elementową listę trzycyfrowymi liczbami pseudolosowymi a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w liście,
dla którego w liście występuje również rewers tego ciągu. Na przykład dla listy:
[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
odpowiedzią jest liczba 4.
Dla podciągu [9,3,1,7] rewersem jest [7,1,3,9].
Wykorzystaj funkcje.
'''
import random

x = input('> ')
while not isinstance(x,int) or x<=0:
    try:
        x=int(x)
    except:
        x=input('Podaj liczbe calkowita: ')
    if isinstance(x,int) and x<0:
        x = input('Podaj liczbe calkowita: ')

tab=[random.randint(100,1000) for _ in range(x)]
#tab=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
tabr=tab[::-1]
print(tab)

maxLen=0
for i in range(len(tab)-1):
    for ii in range(i+1, len(tab)):
        for j in range(len(tab)-1):
            for jj in range(j+1,len(tab)):
                if (ii-i)==(jj-j) and (ii-i)>maxLen and tab[i:ii]!=tab[j:jj]:
                    tab2 = tab[i:ii]
                    tabr2 = tabr[j:jj]
                    if tab2==tabr2:
                        print(tab2, tabr2)
                        maxLen=len(tab2)

print(maxLen)