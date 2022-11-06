'''
Proszę napisać program, który umożliwia zamianę dowolnej liczby naturalnej z jednego systemu liczb w drugi w zależności od wyboru użytkownika (na wejściu).
Należy rozważyć następujące systemy liczbowe: dwójkowy, ósemkowy, dziesiętny, szesnastkowy.
'''
'''
160 10 2 -> 10100000
567123567123 8 16 -> BB94EEE53
10101010111111010101 2 10 -> 700373
'''
def checker(x):
    while not isinstance(x,int) or x<=0:
        try:
            x=int(x)
        except:
            x=input('Podaj liczbe calkowita: ')
        if isinstance(x,int) and x<0:
            x = input('Podaj liczbe calkowita: ')
    return x

n=input('Podaj liczbe: ')

sysPrev=input('Z jakiego systemu jest ta liczba?\n')
sysPrev=checker(sysPrev)

sysNext=input('Na jaki system przeksztalcic?\n')
sysNext=checker(sysNext)

#stworzenie dictionary z odpowiednimi kluczami dla systemow
dOctBin={'0':'000', '1':'001', '2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'}
dBinOct={y:x for x,y in dOctBin.items()}
dHexBin={'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
dBinHex={y:x for x,y in dHexBin.items()}

def binOct(n):
    x=''
    while len(n)%3!=0:
        n='0'+n
    i=0
    while i<=len(n)-3:
        x+=dBinOct.get(n[i:i+3])
        i+=3
    return x

def binDec(n):
    n=int(n)
    x=0
    i=0
    while n!=0:
        x+=(n%2)*(2**(i))
        i+=1
        n//=10
    return x

def binHex(n):
    x = ''
    while len(n) % 4 != 0:
        n = '0' + n
    i = 0
    while i <= len(n) - 4:
        x += dBinHex.get(n[i:i + 4])
        i += 4
    return x

def octBin(n):
    x=''
    for i in n:
        x+=dOctBin.get(i)
    return x

def decBin(n):
    x=0
    cnt=0
    n=int(n)
    while n!=0:
        x*=10
        x+=n%2
        n//=2
        if x==0:
            cnt+=1
    x='0'*cnt+str(x)
    return x[::-1]

def hexBin(n):
    x = ''
    for i in n:
        x += dHexBin.get(i)
    return x

print(f'Twoja liczba przed zamiana: {n}')

if sysPrev==8: n=octBin(n)
elif sysPrev==10: n=decBin(n)
elif sysPrev==16: n=hexBin(n)
elif sysPrev==2: pass
else:
    print('Nie ma takiego systemu w programie, do zobaczenia')
    exit()

if sysNext==2: print(f'Twoja liczba po zamianie: {n}')
elif sysNext==8: print(f'Twoja liczba po zamianie: {binOct(n)}')
elif sysNext==10: print(f'Twoja liczba po zamianie: {binDec(n)}')
elif sysNext==16: print(f'Twoja liczba po zamianie: {binHex(n)}')
else:
    print('Nie ma takiego systemu w programie, aufwiedersehen')
    exit()