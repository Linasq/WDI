'''
Stwórz funkcję, która przyjmuje jako argument listę liczb naturalnych i zwraca sumę liczb z listy, dla których kolejne dzielniki są dzielnikami pierwszymi.

sum_prime([7, 13, 18, 23, 24]) ➞ "(2 42)(3 42)(7 7)(13 13)(23 23)"
sum_prime([3, 5, 7, 9, 11, 13]) ➞ "(3 12)(5 5)(7 7)(11 11)(13 13)"
'''
def sum_prime(tab):
    dict={}
    for i in tab:
        if i>0:
            n=i
            x = 2
            while n!=1:
                if n%x==0:
                    if x in dict.keys():
                        dict[x]+=i
                    else:
                        dict.update({x:i})
                    while n%x==0:
                        n//=x
                x+=1
    return dict

print(f'1: {sum_prime([7,13,18,23,24])}')
print(f'2: {sum_prime([3, 5, 7, 9, 11, 13])}')
print(f'3: {sum_prime([121, 100, 33, 66, 12, 450, 123])}')
print(f'4: {sum_prime([1,1,1,11,1,11,0,0,0,0,1,1,1,11,11])}')
print(f'5: {sum_prime([-7,-13,-18,-23,24])}')