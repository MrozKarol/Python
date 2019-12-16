"""
Napisz program który policzy sumę wszystkich liczb od 1 do
do podanej liczby
"""

def sumuj_do(liczba):
    suma = 0
    for liczba in range(1, liczba + 1):
        suma = suma + liczba
    return suma

def sumuj_do2(liczba):
    
    return sum([liczba
        for liczba in range(1, liczba + 1)

    ])

def sumuj_do3(liczba):
     return int(((1 + liczba) / 2 * liczba))    


print(sumuj_do(5))

print(sumuj_do2(5))

print(sumuj_do3(5))

