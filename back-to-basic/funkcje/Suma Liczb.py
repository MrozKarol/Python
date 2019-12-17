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
     return ((1 + liczba) / 2 * liczba)   


def finish_timer(start):
    end = time.perf_counter()
    return end-start

start = time.perf_counter()
print(sumuj_do(8888))
end = time.perf_counter()
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do2(8888))
end = time.perf_counter()
print(finish_timer(start))

start = time.perf_counter()
print(sumuj_do3(8888))
end = time.perf_counter()
print(finish_timer(start))


start = time.perf_counter()
print(sumuj_do4(8888))
end = time.perf_counter()
print(finish_timer(start))


start = time.perf_counter()
print(sumuj_do5(8888))
end = time.perf_counter()
print(finish_timer(start))

