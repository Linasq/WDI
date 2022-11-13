'''
Proszę napisać program wczytujący 3 liczby całkowite i wskazujący, czy są one zbudowane z takich samych cyfr.
Należy obsłużyć wyjątek, gdy na wejściu zostanie podana liczba niecałkowita
oraz w przypadku gdy wczytane liczby nie są zbudowane z takich samych cyfr należy wygenerować po 3 liczby dla każdej z wczytanych liczb, które byłyby zbudowane ze wskazanych cyfr.
'''
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

#zwracana jest posortowana lista cyfr danej liczby
def putIn(n):
    tab=[int(i) for i in str(n)]
    return sorted(tab)

#generowanie 3 roznych liczb (jesli idzie)
def generateNum(n, tab):
    tabr=[]
    z=n
    if len(set(tab))==1:
        return 'Nie mozna stworzyc innych liczb'
    else:
        if len(str(n))<=3: dl=2
        else: dl=3
        for i in range(dl):
            x = (n % 10) * 10 ** (len(str(n))-1)
            n = (n // 10) + x
            if z!=n: tabr.append(n)
    return  tabr

x,y,z = input('Podaj 3 liczby oddzielone spacja:\n').split()

#3 liczby typu int
x=checker(x)
y=checker(y)
z=checker(z)

#posortowane tablice z liczbami
tabx=putIn(x)
taby=putIn(y)
tabz=putIn(z)

if tabx==taby==tabz:
    print('Twoje liczby sa zbudowane z tych samych cyfr')
else:
    print('Twoje liczby nie sa zbudowane z tych samych cyfr, wiec zbudowalem je za Ciebie:')
    print(f'Dla liczby {x} taki jest wynik: {generateNum(x,tabx)}')
    print(f'Dla liczby {y} taki jest wynik: {generateNum(y,taby)}')
    print(f'Dla liczby {z} taki jest wynik: {generateNum(z, tabz)}')