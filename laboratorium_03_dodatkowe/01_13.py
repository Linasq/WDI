'''
Napisz funkcję, która posortuje dowolny zagnieżdżony słownik (jak w przykładzie ze sklepami i owocami) według jego wartości (cen).
Przykład:
test_dict = {'Lidl' : {'Jabłka' : 5, 'Pomarańcze' :  2, 'Gruszki' : 14},
             'Kaufland' : {'Jabłka' : 15, 'Pomarańcze' :  7, 'Gruszki' : 2},
             'Aldi' : {'Jabłka' : 5, 'Pomarańcze' :  50, 'Gruszki' : 20}}
'''
dc= {'Lidl' : {'Jabłka' : 5, 'Pomarańcze' :  2, 'Gruszki' : 14},
             'Kaufland' : {'Jabłka' : 15, 'Pomarańcze' :  7, 'Gruszki' : 2},
             'Aldi' : {'Jabłka' : 5, 'Pomarańcze' :  50, 'Gruszki' : 20}}

#mozna w 2 linijkach, ale kto to wtedy poczyta
'''
wytlumaczenie co sie dzieje w sorted
na poczatku przekazujemy itemy, jakie musimy posortowac
gdy napiszemy samo value.items() -> to nam posortuje wg klucza
dlatego potrzeba nam wg czego funkcja sorted ma sortowac
sorted, procz tego co ma posortowac rowniez pobiera nieopcjonalnie key oraz reverse
key pomaga nam customizowac nasz output np wg czego ma sortowac
reverse przyjmue wartosci bool, by wiedziec czy ma byc rosnaco, czy malejaco

wiec jak juz wiemy, do czego sluzy key
to uzywamy wlasnie tego keya, i wskazujemy mu wg czego ma sortowac
'''
for key,value in dc.items():
    dcSorted={k:v for k,v in sorted(value.items(), key=lambda item: item[1])}
    dc[key]=dcSorted
print(dc)