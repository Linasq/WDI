'''
Wykorzystując wzór ∑^∞ _n=0 (1/n!)=e, proszę wyznaczyć liczbę e z dokładnością do wpisanej przez użytkownika liczby miejsc dziesiętnych.
Różnice pomiędzy kolejnymi przybliżeniami a przybliżeniem ostatnim należy przechować w liście i na sam koniec wypisać 10 początkowych, 10 środkowych i 10 końcowych elementów listy.
'''
x=input('>')
while not isinstance(x, int) or x<0:
    try:
        x = int(x)
    except:
        x = input('Podaj liczbe calkowita: ')
    if isinstance(x, int) and x<0:
        x = input('Podaj liczbe calkowita: ')

e=2
n=1
i=2
tab=[2]
stop = x if x >16 else 100
while len(str(e))-2<x:
    n*=i
    i+=1
    e+=(1/n)
    tab.append(e)
    if i ==stop:
        break
tabR=[tab[-1]-i for i in tab]
print(f'Pierwsza dycha:\n{tabR[:10]}\nTeraz cos ze srodeczka:\n{tabR[int(len(tabR)/2)-5:int(len(tabR)/2)+5]}\nI koncowka:\n{tabR[-10::]}')
