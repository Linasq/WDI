'''
Proszę napisać program, który umożliwia obliczenie wartości N! dla N zakresu od 1 do M,
gdzie M jest wartością wpisaną przez użytkownika.
Należy obsłużyć wyjątek, gdy użytkownik podaje liczbę mniejszą od 1 oraz taki gdy M jest większe od 10000.
Program powinien też wypisywać na końcu różnice pomiędzy kolejnymi wartościami N!.
'''
x=input('>')
while not isinstance(x, int) or x<1 or x>10000:
    try:
        x = int(x)
    except:
        x = input('Podaj liczbe calkowita: ')
    if isinstance(x, int) and (x<1 or x>10000):
        x = input('Podaj liczbe calkowita: ')

silnia=1
sliniaPrev=silnia

#wypisanie kolejnych silni oraz roznicy miedzy i! oraz (i-1)!
for i in range(1,x+1):
    silniaPrev=silnia
    silnia*=i
    z=f'{i}! = {silnia}, a {i}!-{i-1}! = {silnia-silniaPrev}' if i!=1 else f'{i}! = {silnia}'
    print(z)