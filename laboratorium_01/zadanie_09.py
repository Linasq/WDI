with open('zadanie_09.txt', 'r') as f:
    saldo=int(f.readline())

print('*'*10+' Witamy w najlepszym banku! '+'*'*10)
print('Na poczatku wybierz, co chcialbys zrobic?')

pin=1234
wyjscie=['0', 'wyjscie', 'exit', 'quit', 'wyjście']
wplata=['1', 'wplata', 'wpłata']
wyplata=['2', 'wyplata', 'wypłata']
konto=['3', 'saldo', 'stan konta', 'konto', 'ile']

def zapisSalda(n):
    with open('zadanie_09.txt', 'w') as f:
        f.write(str(n))

def sprawdzPin(n):
    if n!=pin:
        n=int(input('Podaj poprawny kod PIN: '))
        sprawdzPin(n)
    return True

def zapytania():
    global saldo
    x = input('1. Wplata pieniedzy\n2. Wyplata pieniedzy\n3. Sprawdz stan konta\n')
    kodPin=int(input('Podaj kod PIN: '))
    if sprawdzPin(kodPin):
        if x.lower() in wyjscie:
            zapisSalda(saldo)
            quit()
        elif x.lower() in wplata:
            ile = int(input('Ile chcesz wplacic na konto: '))
            if ile<=0:
                print('Nie mozna wplacic liczby mniejszej od 0!!!\nSprobuj jeszcze raz')
                zapytania()
            else:
                saldo += ile
                print('Pomyslnie wplacono pieniadze!\n')
                zapisSalda(saldo)
        elif x.lower() in wyplata:
            ile = int(input('Ile chcesz wyplacic: '))
            if ile>saldo:
                print('Blad!! Nie mozna wyplacic wiecej, niz sie ma na koncie. Sprobuj jeszcze raz.\n')
                zapytania()
            else:
                saldo -= ile
                zapisSalda(saldo)
                print('Pomyslnie wyplacono pieniadze!\n')
        elif x.lower() in konto:
            print(f'Aktualny stan konta: {saldo}\n')
        else:
            print('Nie ma takiej komendy, sprobuj jeszcze raz.\n')
            zapytania()

zapytania()
while True:
    print('Co chcesz zrobic w nastepnym kroku?\n')
    zapytania()