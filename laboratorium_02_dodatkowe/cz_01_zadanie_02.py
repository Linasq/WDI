'''
Proszę napisać program, który metodą sita Eratostenesa wyznaczy liczby pierwsze mniejsze od N (wczytywane).
Należy obsłużyć wyjątek wczytania liczby, która nie jest naturalna i podać ilorazy całkowite i reszty kolejnych wyznaczonych liczb pierwszych,
przy założeniu, że dzielimy większą liczbę przez mniejszą.
'''
x = input('> ')
while not isinstance(x,int) or x<=0:
    try:
        x=int(x)
    except:
        x=input('Podaj liczbe calkowita: ')
    if isinstance(x,int) and x<0:
        x = input('Podaj liczbe calkowita: ')

#uzupelnienie tablicy wartosciami prawdziwymi
tab=[True for _ in range(2,x)]
dl=len(tab)

#sito tego chopka, False -> liczba nie jest pierwsza
for i in range(dl):
    if tab[i]:
        z=i+2
        z += (i + 2)
        while z<dl+2:
            if tab[z-2]:
                tab[z-2]=False
            z += (i + 2)

#podanie ilorazow calkowitych i reszty kolejnych liczby pierwszych
x=2
for i in range(1,dl):
    if tab[i]:
        y=i+2
        print(f'Iloraz: {y//x}, reszta: {y%x}')
        x=y
