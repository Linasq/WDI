'''
Należy napisać program, który umożliwia zmianę nazw, kopiowanie, przenoszenie i usuwanie plików zgodnie z życzeniem użytkownika.
Można skorzystać z modułu os.
Program powinien poprosić użytkownika o hasło a następnie porównać je z zahashowanym hasłem znajdującym się w pliku /home/my_hashed_password.txt.
Należy skorzystać z modułu hashlib.
Należy obsłużyć niezbędne wyjątki.
'''
import os
import hashlib

#tablica, gdzie nie moze user debil wchodzic
tabZlych=['/bin','/dev','/lib','/mnt','/root','/snap','/sys','/var','/boot','/etc','/lib32','/opt','/run','/srv','/tmp','/cdrom','/lib64','/media','/proc','/sbin','/swapfile','/usr', '/..']

#walidacja inputu
def walidacja(x):
    while not isinstance(x,int) or x<=0:
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int) and x<=0:
            x = input('Podaj liczbe calkowita: ')
    return x

#sprawdzamy, czy haslo jest to samo
def checker(n):
    try:
        with open('/home/my_hashed_password.txt', 'r') as f:
            s=f.readline().split()
            if s[0]==n: return True
            return False
    except:
        exit('Brak pliku')

def where(n):
    global tabZlych
    for i in tabZlych:
        if n[0:len(i)-1]==i: exit('Nie ma tak latwo')
        else: return True

#poczatek programu, uzytkownik jest proszony o podanie hasla, 3 nieprawidlowe proby i user jest out
def passy():
    print('Podaj haslo')
    for i in range(3):
        n=hashlib.md5(input('>').encode()) #haslo jest hashowane od razu od inputu
        if checker(n.hexdigest()): return True
        elif i<2:
            print(f'Haslo niepoprawne, masz jeszcze {3-i-1} proby')
        else:
            exit('Poznaj najpierw haslo, potem wroc')

#funkcja od ktorej sie wszystko zaczyna
def main():
    if passy():
        zapytanie=walidacja(input('Wybierz akcje:\n1. Zmiana nazwy pliku\n2. Kopiowanie pliku\n3. Przenoszenie pliku\n4. Usuwanie pliku\n'))
        if zapytanie==1:
            zmianaNazwy()
        elif zapytanie==2:
            kopiowaniePliku()
        elif zapytanie==3:
            przenoszeniePliku()
        elif zapytanie==4:
            usunPlik()
        else: exit('Nie ma takiego polecenia')

#funkcja, ktora zmienia nazwe pliku
def zmianaNazwy():
    name=input('Podaj nowa nazwe: ')
    if not '.txt' in name: name+='.txt'
    file=input('Na ktorym pliku ma to miec efekt (sciezka): ')
    if where(file):
        tab = file.split('/')
        tab[-1] = name
        newFile = ''
        for i in tab:
            newFile += i
            if not '.txt' in i:newFile += '/'
        try: os.rename(file,newFile)
        except: exit('Nieprawidlowa sciezka do pliku')

#funkcja, ktora kopiuje plik
def kopiowaniePliku():
    oldFile=input('Podaj stara sciezke: ')
    newFile=input('Podaj nowa sciezke: ')
    if where(oldFile) and where(newFile):
        os.chdir('/home/linas/')
        os.popen(f'cp {oldFile} {newFile}')

#TODO wszystkie funkcje zrobic w jednym i uzyc os.popen
#funkcja, ktora przenosi plik
def przenoszeniePliku():
    oldFile = input('Podaj stara sciezke: ')
    newFile = input('Podaj nowa sciezke: ')
    if where(oldFile) and where(newFile):
        os.chdir('/home/linas/')
        os.popen(f'mv {oldFile} {newFile}')

#funkcja, usuwajaca plik
def usunPlik():
    file=input('Podaj plik od usuniecia: ')
    if where(file):
        try: os.remove(file)
        except: exit(f'Permission denied or there is no file "{file}"')

main()