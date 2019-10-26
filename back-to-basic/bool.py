# print('Porównywarka liczba')

# a = int(input('Wpisz liczbę a: '))
# b = int(input('Wpisz liczbę b: '))

# if (a>b):
#     print('a jest wieksze od b')
# elif (b>a):
#     print('b jest wieksze od a')
# else:
#     print('a jest równe b') 

wybor = int(input('''Wybierz działanie:
1- mnozenie, 2-dzielenie,
3- dodawanie, 4-odejmowane
5- potęgowanie 
'''))
a = int(input('Wpisz liczbę a: '))
b = int(input('Wpisz liczbę b: '))


if (wybor == 1):
    print('Wynik z mnożenia to', str(a * b))
elif (wybor == 2):
    if(b == 0):
        print('NIE dziel przez zero :(')
        b = int(input('Wpisz jeszcze raz liczbę b: '))
    print('Wynik z dzielenia to', str(a / b))
elif (wybor == 3):
    print('Wynik z dodawania to', str(a + b))
elif (wybor == 4):
    print('Wynik z odejmowania to',str(a - b))
elif (wybor == 5):
    print('Wynik z potęgowania to', str(a**b))       
else:
    print('nie wybrałeś dobrego wybru')