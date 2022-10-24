#komentarz
'''
suma, roznica, iloczyn, iloraz, kwadrat, pierwiastek
'''
a,b = input('Podaj dwie liczby: ').split()
a=int(a)
b=int(b)
if a<0 and b<0:
    print("Paaanie, ale tak nie mozna, dej Pan dodatnie liczby")
else:
    if a<0:
        a*=-1
    elif b<0:
        b*=-1
    suma = a+b
    roznica = a-b
    iloczyn = a*b if a*b!=10 else str(a*b)+' Yay!'
    iloraz = a/b if b!=0 else 'Nie mozna dzielic przez 0!!'
    potA = a**2
    potB = b**2
    sqA = a**0.5
    sqB = b**0.5
    print(f'Suma: {suma}\nRoznica: {roznica}\nIloczyn: {iloczyn}\nIloraz: {iloraz}\nKwadrat liczby A {potA}, B {potB}\nPierwiastek liczby A {sqA}, B {sqB}')