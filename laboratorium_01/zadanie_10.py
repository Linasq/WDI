import random

def obliczenia():
    x,y = input('Podaj dwie liczby: ').split()
    sym = input('Podaj jeden z symboli wypisanych ponizej\n+ - * / # ^ x\n')
    x = int(x)
    y = int(y)
    if sym=='+':
        print(x+y)
    elif sym == '-':
        print(x-y)
    elif sym == '*':
        print(x*y)
    elif sym=='/':
        if y==0:
            print('Nie wolno dzielic przez 0!!!!')
        else:
            print(round(x/y,4))
    elif sym =='#':
        if x<0 and y%2==0:
            print('Ten kalkulator nie lubi liczb zespolonych ;)')
        else:
            print(x**(1/y))
    elif sym =='^':
        print(x**y)
    elif sym =='x':
        if x<y:
            print(random.randint(x,y))
        else:
            print(random.randint(y,x))
    else:
        print('Nie ma takiego symbolu')

obliczenia()
while True:
    w = input('Czy chcesz wprowadzic nowe dane?\n')
    if w.lower() == 't' or w.lower()=='y' or w.lower()=='':
        obliczenia()
    elif w.lower()=='n':
        quit()
    else:
        print('Nie rozumiem')