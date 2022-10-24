x = int(input('Podaj liczbe zaczynajaca zakres: '))
y = int(input('Podaj liczbe konczaca zakres: '))
if y-x>20:
    srednia = (x+y)/2
    n=int(srednia+3)
    count=0
    # wykorzystujemy to, ze nie ma napisane jak ten zakres nalezy wypisac
    while count<6:
        if n!=srednia:
            print(n)
            n-=1
            count+=1
        else:
            n-=1
else:
    for i in range(x,y+1):
        print(i)