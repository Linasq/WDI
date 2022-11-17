'''
Dana jest N-elementowa lista zawierająca liczby naturalne mniejsze od 1000.
Proszę napisać funkcję, która zwraca długość najdłuższego spójnego fragmentu listy, dla którego w iloczynie jego elementów każdy czynnik pierwszy występuje co najwyżej raz.
Na przykład dla listy lista_1 = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22] wynikiem jest wartość 5. Przykład iloczynu elementów dla fragmentu [2,23,33] to 1∗2∗1∗23∗1∗3∗11.
'''
import random

def finder(t):
    n=len(t)
    i,j=1,0
    currNum,maxCiag,cnt=t[0],1,1
    while i<n:
        if isValid(currNum,t[i]):
            currNum*=t[i]
            i+=1
            cnt+=1
            if cnt>maxCiag: maxCiag=cnt
        else:
             if currNum==1:
                i+=1
                j+=1
             else:
                cnt-=1
                currNum//=t[j]
                j+=1
    return maxCiag

def isValid(currNum, x):
    if currNum%x==0:
        return False
    k=2
    isDivided=False
    while x>1:
        if x%k==0:
            x//=k
            if currNum%k==0 or isDivided:
                return False
            isDivided=True
        else:
            k+=1
            isDivided=False
    return True

#walidacja liczby
x=input('Podaj dlugosc listy: ')
while not isinstance(x, int) or x <= 0:
    try:
        x = int(x)
    except:
        x = input('Podaj liczbe calkowita: ')
    if isinstance(x, int) and x < 0:
        x = input('Podaj liczbe calkowita: ')

tab=[random.randint(1,1000) for _ in range(x)]

tabTest=[13,11,12,5,6,14,2,5,7,11,13,17,19,22]

lista_1 = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]

print(tab)
print(finder(tab))

print(tabTest)
print(finder(tabTest))

print(lista_1)
print(finder(lista_1))