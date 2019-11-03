'''
len() długiść
.append - dodać element na koncu listy
.extend - rozszerzy listę o elementy
.insert(index,co) wstawić
.index - index dodanego el.
sort(reverse=Fale) - sortuj rossnąco
max()
min()
.count - ile razy coś wystąpi
.pop - usuń pierwsze wystąpienie
.remove - usuń pierwsze wystąpienie
.clear - wyczyść liste
.reverse - zmień kolejność
'''


lista1 = [53, 1, -2, 20, 1]
lista2 = ['Karol', 'Magdalena']

print('Ponieżej listy na których wykonasz operacje: \n' , lista1, '\n', lista2)

x = int(input("Wybierz co chesz zrobić: 1 - len() -długość, 2 - append - dodać element na koncu listy \n 3- .extend rozszerzy liste o elementy 4- .insert(index,co) wstawić: "))


if ( x == 1):
    y = str(input('Wpisz lisa1 lub lista2'))
    if(y == 'lista1'):
        print(len(lista1))
    elif (y == 'lista2'):
        print(len(lista2))    

elif ( x == 2):
    y = str(input('Wpisz lisa1 lub lista2'))
    if(y == 'lista1'):
        append = input("Wpisz co chcesz dodać : ")
        lista1.append([append])
        print(lista1)
    elif (y == 'lista2'):
        append = input("Wpisz co chcesz dodać : ")
        lista2.append([append])
        print(lista2)
elif (x == 3):
    y = str(input('Wpisz lisa1 lub lista2'))
    if(y == 'lista1'):
        extend = input("Wpisz co chcesz dodać: ")
        lista1.extend([extend])
        print(lista1)
    elif (y == 'lista2'):
        extend = str(input("Wpisz co chcesz dodać: "))
        lista2.extend([extend])
        print(lista2)
elif (x == 4):
    y = str(input('Wpisz lisa1 lub lista2: '))
    if(y == 'lista1'):
        insert= int(input('Wpisz co chcesz dodać:'))
        lista1.insert(0,insert)
        print(lista1)
    elif (y == "lista2"):
        insert= str(input('Wpisz co chcesz dodać:'))
        lista2.insert(0,insert)
        print(lista2)

