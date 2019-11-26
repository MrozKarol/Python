'''
Napisz program który pozwoli użytkownikowi:
1.Dodawać nowe definicje 
2. Szukać instniejących definicji
3. Usuwać wybrane przez niego definicje

'''
definicje = {}
while (True):
    print('1": Dodać definicje')

    print('2": Znajdź definicje')

    print('3": Usuń definicje')

    print('4: Zakończ')

    print('5: Wyświetl wszystike dodane klucze i słowa')

    wybor = input('Co chcesz zrobić ?')


    if (wybor == '1'):
        klucz = input('Podaj klucz słowo do zdefiniowania')
        definicja = input ('Podaj definicję ')
        definicje[klucz] = definicja
        print('Definicja podana pomyślnie')
    elif (wybor == '2'):
        klucz = input('Czego szukasz ?')
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print('Nie znaleziono definicji o nazwie', klucz)
    elif (wybor == '3'):
        klucz = input('Jaką definicję chesz usunąć')
        if klucz in definicje:
            del definicje[klucz]
            print('Usunięto definicję o nazwie', klucz)
        else:
            print('Nie znaleziono definicji o nazwie', klucz)
    elif (wybor == '4'):
        print('Koniec programu')
        break            
    elif (wybor == '5'):
        print(definicje)
    else:
        print('Podałeś coś z poza zakresu')    
