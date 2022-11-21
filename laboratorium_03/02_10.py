'''
Wykorzystując funkcje, proszę napisać program, który pobiera przykładowy tekst zapisany w pliku, np.: lorem ipsum...
A następnie zwraca wartość określającą liczbę wyrazów w danym tekście. Można w tym celu skorzystać z wyrażeń regularnych.
'''
with open('lorem.txt', 'r') as f:
    tab=f.read().split()
print(len(tab))
tab=[i.strip(',. ():?!;…-—').lower() for i in tab]
dc={k:tab.count(k) for k in tab}
print(dc)