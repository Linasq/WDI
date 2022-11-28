'''
Wykorzystując bibliotekę pandas, załaduj plik iris.csv do ramki danych (dataframe).
Wyświetl pojedyncze punkty ze zbioru danych na 4 wykresach (każdy z parametrów z każdym) punktowych.
Punkty powinny mieć różne kolory w zależności od gatunku irysa (class).
Wykorzystaj funkcję plot.scatter().
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv', delimiter=',')

#podzielenie data framu na ramki z poszczegolnymi kwiatkami
IrisSetosa=df[df['class']=='Iris-setosa']
IrisVersicolor=df[df['class']=='Iris-versicolor']
IrisVirginica=df[df['class']=='Iris-virginica']

#konfigurowanie kazdego z kwiatow
setosa1=IrisSetosa['sepallength']
setosa2=IrisSetosa['sepalwidth']
setosa3=IrisSetosa['petallength']
setosa4=IrisSetosa['petalwidth']

versicolor1=IrisVersicolor['sepallength']
versicolor2=IrisVersicolor['sepalwidth']
versicolor3=IrisVersicolor['petallength']
versicolor4=IrisVersicolor['petalwidth']

virginica1=IrisVirginica['sepallength']
virginica2=IrisVirginica['sepalwidth']
virginica3=IrisVirginica['petallength']
virginica4=IrisVirginica['petalwidth']

#zaczynamy plotting
plt.figure('sepallength') #pierwszy wykres
plt.title('Sepal length')
plt.xlabel('id')
plt.ylabel('length (cm)')
plt.plot(setosa1, 'ro', label='Iris-setosa')
plt.plot(versicolor1, 'bo', label='Iris-versicolor')
plt.plot(virginica1, 'go', label='Iris-virginica')
plt.legend(loc = 'upper left')

plt.figure('sepalwidth') #drugi wykres
plt.title('Sepal width')
plt.xlabel('id')
plt.ylabel('width (cm)')
plt.plot(setosa2, 'ro', label='Iris-setosa')
plt.plot(versicolor2, 'bo', label='Iris-versicolor')
plt.plot(virginica2, 'go', label='Iris-virginica')
plt.legend(loc = 'upper left')

plt.figure('petallength') #trzeci wykres
plt.title('Petal length')
plt.xlabel('id')
plt.ylabel('length (cm)')
plt.plot(setosa3, 'ro', label='Iris-setosa')
plt.plot(versicolor3, 'bo', label='Iris-versicolor')
plt.plot(virginica3, 'go', label='Iris-virginica')
plt.legend(loc = 'upper left')

plt.figure('petalwidth') #czwarty wykres
plt.title('Sepal width')
plt.xlabel('id')
plt.ylabel('width (cm)')
plt.plot(setosa4, 'ro', label='Iris-setosa')
plt.plot(versicolor4, 'bo', label='Iris-versicolor')
plt.plot(virginica4, 'go', label='Iris-virginica')
plt.legend(loc = 'upper left')

plt.show()