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
3- dodawanie, 4-odejmowane: 
'''))
a = int(input('Wpisz liczbę a: '))
b = int(input('Wpisz liczbę b: '))

print(type(wybor))

if (wybor == 1):
    print(a * b)
elif (wybor == 2):
    if(b == 0):
        print('NIE dziel przez zero :(')
        b = int(input('Wpisz jeszcze raz liczbę b: '))
    print(a / b)
elif (wybor == 3):
    print(a + b)
elif (wybor == 4):
    print(a - b)   
else:
    print('nie wybrałeś dobrego wybru') 