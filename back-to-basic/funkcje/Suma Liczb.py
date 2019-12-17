"""
Napisz program który policzy sumę wszystkich liczb od 1 do
do podanej liczby
"""
"""
Mierzenie wydajności kodu
"""

import time

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
    
    return sum({liczba
        for liczba in range(1, liczba + 1)
    })

def sumuj_do4(liczba):
    
    return sum((liczba
        for liczba in range(1, liczba + 1)
    ))

def sumuj_do5(liczba):
     return int(((1 + liczba) / 2 * liczba))    

start = time.perf_counter()
print(sumuj_do(5))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(sumuj_do2(5))
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
print(sumuj_do3(5))
end = time.perf_counter()
print(end-start)


start = time.perf_counter()
print(sumuj_do4(5))
end = time.perf_counter()
print(end-start)


start = time.perf_counter()
print(sumuj_do5(5))
end = time.perf_counter()
print(end-start)

