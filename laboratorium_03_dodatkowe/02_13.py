'''
Wykorzystując bibliotekę pandas, załaduj plik iris.csv do ramki danych (dataframe).
Oblicz średnią, medianę, wyfiltruj wartości petallength ≥ od wartości wskazanej przez użytkwnika.
Po tych operacjach pokaż ramkę danych skorzystaj z funkcji head(), tail(), describe(). Co one robią?
'''
import pandas as pd

#walidacja liczby podanej od uzytkowanika, liczba zmiennoprzecinkowa
def checker(x):
    while not isinstance(x,float):
        try:
            x=float(x)
        except:
            x=input('Podaj liczbe calkowita: ')
    return x

x=checker(input('Wartosci petallength > '))

data=pd.read_csv('iris.csv', delimiter=',') #pobranie pliku csv
print(data[['sepallength','sepalwidth','petallength','petalwidth']].mean()) #srednia arytmetyczna wszystkich rzeczy, do ktorych mozna bylo uzyskac srednia
print(data[['sepallength','sepalwidth','petallength','petalwidth']].median()) #mediana wszystkich liczb
print(data['petallength'][data['petallength']>=x]) #wyfiltrowanie z kolumny petallen liczb, ktore sa wieksze od x i wyswietlenie tylko kolumny petallen
print(data.head()) #wypisuje pierwsze 5 wierszy
print(data.tail()) #wypisuje ostatnie 5 wierszy
print(data.describe()) #tworzy krotki opis nt pliku (srednia, mediana, min, max, odchylenie etc)