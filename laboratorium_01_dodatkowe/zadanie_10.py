'''
Proszę napisać program, który oblicza pole figury pod wykresem funkcji: y=1/x
w przedziale od 1 do k, metodą prostokątów. Od użytkownika pobierane jest k.

Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
Należy obsłużyć wyjątek wczytania 0.
'''
x = input('Podaj liczbe: ')
while not isinstance(x,int) or x<=0:
    try:
        x=int(x)
    except:
        x=input('Podaj liczbe calkowita: ')
    if isinstance(x,int) and x<0:
        x = input('Podaj liczbe calkowita: ')

s=0
i=0.000001
k=i
while i<x:
   if 1/i - 1/(i+k)<k:
       n=k*(1/i)
       s+=n
   i+=k
print(s)