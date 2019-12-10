a = int(input('podaj bok a:'))
b = int(input('podaj bok b:'))

def pole_prostokonta(a, b):
    if(a == b):
        print('Pole kwadratu równa sie' , (a * b))
    elif(a != b):
        print('Pole prostokonta równa sie' , (a * b))
     


pole_prostokonta(a, b)