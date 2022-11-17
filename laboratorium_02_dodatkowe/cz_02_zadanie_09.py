'''
Liczba półpierwsza to liczba, która jest iloczynem dwóch liczb pierwszych (niekoniecznie różnych).
Stwórz funkcję, która przyjmuje pobraną od użytkownika liczbę N jako argument i zwraca dwie listy.
Pierwsza to z liczbami półpierwszymi <N, które są iloczynem dwóch różnych liczb pierwszych a druga z pozostałymi liczbami półpierwszymi <N.
Wykorzystaj odwzorowanie list.
'''
def isPrime(n):
    if n == 2: return True
    elif n<2 or n%2==0: return False
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0: return False
    return True

def polpierwsze(x):
    tab = [i for i in range(int(x ** 0.5) + 1) if isPrime(i)]

    # tablica liczb polpierwszych rownych liczb i roznych liczb
    tabPP = []
    tabPPR = []
    for i in tab:
        for j in tab:
            if i ==j: tabPPR.append(j*i)
            elif i*j not in tabPP: tabPP.append(j*i)
    return tabPP,tabPPR

#walidacja liczby
x=input('Liczby polpierwsze mniejsze od:  ')
while not isinstance(x, int) or x <= 0:
    try:
        x = int(x)
    except:
        x = input('Podaj liczbe calkowita: ')
    if isinstance(x, int) and x < 0:
        x = input('Podaj liczbe calkowita: ')

print(polpierwsze(x))