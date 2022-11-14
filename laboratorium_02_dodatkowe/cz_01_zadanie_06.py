'''
Proszę napisać program wczytujący z klawiatury dowolną ilość znaków.
Program powinien wybrać tylko te znaki, które znajdują się pomiędzy zerami.
Np. po wpisaniu “dsgdfhfdghd0ewjhefbbnf0erffgg” interesujący dla programu będzie jedynie fragment “ewjhefbbnf”.
Następnie należy wczytane znaki zamienić na kod dziesiętny ASCII wykorzystując funkcję ord().
Należy sprawdzić i wypisać kody a następnie podać znak, który ma 5 co do wartości kod dziesiętny ASCII
(“5, co do wartości” oznacza tutaj –5 “od góry” po posortowaniu).
Można założyć, że dane są poprawne i w ciągu znajduje się wystarczająca liczba elementów.
'''
#ciag='dsgdfhfdghd0ewjhefbbnf0erffgg'
ciag=input('>')

tab=ciag.split('0')
ciagTrue=tab[1] #string majacy tylko nasz ciag

tabASCII=[]
for i in ciagTrue:
    tabASCII.append(ord(i))
