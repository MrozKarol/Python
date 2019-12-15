import math
"""
Program liczący powierzchnie figur
"""

wybor = input('Wybierz pole figury króre chcesz obliczyć\nk - kwadrat\np - prostokąt\nko-koło')
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

if(wybor == 'k'):
    k_bok = float(input('Podaj długość boku'))
    pole = pole_kwadratu(k_bok)
    if(pole > 0):
        print('Pole kwadratu o boku', k_bok, 'równa się', pole)
    else:
        print(error)

if(wybor == 'p'):
    a = float(input('Podaj długość boku a'))
    b = float(input('Podaj długość boku b'))
    if( a > 0 and b > 0 ):
        pole = pole_prostokata(a,b)
        print('Pole prostokąta o bokach', a, b, 'równa się', pole )
    else:
        print(error)

if(wybor == "ko"):
    r = float(input('Podaj promień koła'))
    if(r > 0):
        pole = pole_kola(r)
        print('Pole koła o promieniu', r , 'rówa się', pole)
    else:
        print(error)    
    
                 
    
        

      