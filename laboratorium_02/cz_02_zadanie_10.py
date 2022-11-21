'''
Stwórz funkcję, która przyjmuje jako argument listę liczb naturalnych i zwraca sumę liczb z listy, dla których kolejne dzielniki są dzielnikami pierwszymi.

sum_prime([7, 13, 18, 23, 24]) ➞ "(2 42)(3 42)(7 7)(13 13)(23 23)"
sum_prime([3, 5, 7, 9, 11, 13]) ➞ "(3 12)(5 5)(7 7)(11 11)(13 13)"
sum_prime([121, 100, 33, 66, 12, 450, 123]) -> {11: 220, 2: 628, 5: 550, 3: 684, 41: 123}
sum_prime([1,1,1,11,1,11,0,0,0,0,1,1,1,11,11]) -> {11: 44}
sum_prime([-7,-13,-18,-23,24]) -> {2: 24, 3: 24}
sum_prime([12345678987654321, 1234567898765432112, 12334531254323, 8798797979878751231]) -> {3: 1246913577753086433, 37: 12345678987654321, 2: 1234567898765432112, 7: 1234567898765432112, 11839: 1234567898765432112, 310356383353: 1234567898765432112, 17: 12334531254323, 599: 12334531254323, 1211286581: 12334531254323, 59: 8798797979878751231, 213235447: 8798797979878751231, 699377947: 8798797979878751231}
'''
def sum_prime(tab):
    dict={}#stworzenie slownika, ktory przechowa nasze rozwiazanie
    for i in tab:
        if i>0:
            n=i
            x = 2 #czynnik pierwszy
            while n!=1 and x**2<n:
                if n%x==0:
                    if x in dict.keys(): #jesli juz jest taki czynnik pierwszy w tablicy liscie, to dodajemy do sumy kolejna liczbe
                        dict[x]+=i
                    else: #a jesli nie ma takiego czynnika, to uzupełniamy slownik o nowy czynnik
                        dict.update({x:i})
                    while n%x==0:#dzielimy n przez dany czynnik, dopoki juz nie bedzie podzielny, by uniknac czynnikow typu 4, 6 etc
                        n//=x
                x+=1
            if x**2>n: dict[n]=i
    return dict

print(f'1: {sum_prime([7,13,18,23,24])}')
print(f'2: {sum_prime([3, 5, 7, 9, 11, 13])}')
print(f'3: {sum_prime([121, 100, 33, 66, 12, 450, 123])}')
print(f'4: {sum_prime([1,1,1,11,1,11,0,0,0,0,1,1,1,11,11])}')
print(f'5: {sum_prime([-7,-13,-18,-23,24])}')
print(f'6: {sum_prime([12345678987654321, 1234567898765432112, 12334531254323, 8798797979878751231])}')