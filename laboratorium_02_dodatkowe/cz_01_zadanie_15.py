'''
Wykorzystując odwzrowanie słowników stwórz słowniki,
w którym kluczami są kolejne liczby pierwsze a wartościami liczba znaków potrzebnych do zaprezentowania tych liczb
w systemie dwójkowym, ósemkowym i szesnastkowym (w zależności od wyboru użytkownika).
Na koniec stwórz słownik, który przechowuje informację o tym, ile liczb wymagających konkretnej liczby znaków (w danym systemie) jest.
'''
# do zrobienia tego, wykorzystam liczby pierwsze mniejsze od 1000
def isPrime(n):
    if n==2:
        return True
    elif n<2 or n%2==0:
        return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0: return False
    return True

#zlicza ilosc znakow w zapisie binarnym n-liczba, z-binarne/osemkowe/szesnastkowe
def decChange(n,z):
    cnt=0
    while n!=0:
        cnt+=1
        n//=z
    return cnt

tabPierwsze=[i for i in range(1000) if isPrime(i)]

kod=input('Na jaki system zamienic: ')

if kod=='2' or kod=='8' or kod=='16':
    tabIlosc=[decChange(i,int(kod)) for i in tabPierwsze]
else:
    print('Nie ma takiego systemu zapisanego w pamieci')
    quit()

#slownik zawierajacy liczby pierwsze i ilosc cyfr/liter sluzacych do jego zapisania
dcPierwszych={k:v for k,v in zip(tabPierwsze, tabIlosc)}

#slownik zawierajacy dlugosc zapisu danej liczby i ilosc wystapnienia tej dlugosci
dcIlosc={k:0 for k in dcPierwszych.values()}
for i in dcPierwszych.values():
    dcIlosc[i]+=1
print(dcIlosc)