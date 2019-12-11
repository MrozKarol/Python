import math
"""
Program liczący powierzchnie figur
"""

wybor = input('Wybierz pole figury króre chcesz obliczyć')
error = 'coś poszło nie tak'

def pole_kwadratu(a):
    return a * a

def pole_prostokata(a, b):
    return a * b

def pole_kola(r):
    return math.pi * r ** 2

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):
    return (a + b) / 2 * h

if(wybor == 'a'):
    a_bok = int(input('Podaj długość boku'))
    pole = pole_kwadratu(a_bok)
    if(pole > 0):
        print('Pole kwadratu o boku', a_bok, 'równa się', pole)
    else:
        print(error)
     
    
        

      