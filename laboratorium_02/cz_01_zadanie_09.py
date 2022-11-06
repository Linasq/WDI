'''
Proszę napisać program, który pobierze od użytkownika 5 różnych liczb całkowitych i doda je do listy.
Program ma za zadanie uzupełnić listę liczbami całkowitymi znajdującymi się pomiędzy kolejnymi liczbami a następnie wypisać listę. Przykładowe dane wejściowe:
[0,7,13,8,12]
pożądane wyjście:
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,9,10,11,12].
Należy obsłużyć wyjątek, w którym dwie sąsiadujące ze sobą wprowadzone przez użytkownika liczby są takie

1. [0,7,13,8,12] -> [0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,9,10,11,12]
2. [0,7,-13,20,21] -> [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
3. [12,13,12,13,12] -> [12, 13, 12, 13, 12]
'''
def trying(n):
    x=input(f'Podaj {n} liczbe: ')
    while not isinstance(x,int):
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
    return x

def numbers(x,y):
    tab=[]
    if x<y: z=1
    else: z=-1
    for i in range(x,y,z):
        tab.append(i)
    return tab
tab=[]
x=0
for i in range(5):
    if i==0:
        x=trying(i+1)
    else:
        y=trying(i+1)
        while x==y:
            y=trying(i+1)
        tabTemp=numbers(x,y)
        tab+=tabTemp
        x=y
if tab[-1]!=y:
    tab.append(y)
print(tab)