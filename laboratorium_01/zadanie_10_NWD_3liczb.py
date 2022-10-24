a,b,c = input('Podaj 3 liczby, komputer obliczy NWD\n').split()
a=int(a)
b=int(b)
c=int(c)
def nwd(a,b):
    while b!=0:
        c=b
        b=a%b
        a=c
    return a

print(f'NWD liczb {a}, {b}, {c} wynosi: {nwd(nwd(a,b),c)}')