# Napisz program, który doda kolejne 3 parzyste liczby dodatnie podane przez użytkownika


wynik = 0
i=0

while i < 3:
    x = int(input('Podaj liczbę parzysta: '))
    if (x%2 == 0 and x > 0):
        wynik += x
    else:
        wybor = str(input('Miałabyć być liczba parzysta, wyśnij a żeby kontynuować b żeby przerwać: '))
        if(wybor == 'a'):
            continue
        elif (wybor == 'b'):
            print('Koniec programu')
            break
    i += 1
print('Wynik to:', wynik, 'z', i, 'dodań') 


   