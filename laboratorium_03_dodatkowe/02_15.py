'''
Wykorzystując bibliotekę pandas, załaduj plik iris.csv do ramki danych (dataframe).
Wykonaj operacje dodawania i mnożenia na zbiorze.
Dla każdej z operacji stwórz nowe kolumny.
Wykonaj też operacje odejmowania, dzielenia pomiędzy dwoma wierszami, a wyniki zapisz w istniejącej kolumnie.
Tak powstałą ramkę danych zapisz do nowego pliku.
'''
import pandas as pd

df = pd.read_csv('iris.csv')
seriesSuma=pd.Series(df['sepallength']+df['sepalwidth']+df['petallength']+df['petalwidth']) #zamiast tego moglem od razu zrobic df['suma]=df.sum(axis=1)
seriesMnozenie=pd.Series(df['sepallength']*df['sepalwidth']*df['petallength']*df['petalwidth'])
df['Suma']=seriesSuma
df['Iloczyn']=seriesMnozenie
print(df)

df.to_csv('newCSV.csv')
'''nie jest zrobione w calosci, nie wiem co chce prowadzacy'''
