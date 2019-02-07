# Demonstruje tworzenie krotek
# inwentarz bochatera

# utwórz krotke zawierajaca elementy i wyswietl za pomocą petli for


inventory =("miecz zagłady",
            "wypasiona zbroja",
            "tarcza szmato",
            "gumijagody")
for item in inventory:
    print(item)

# wyświetl długość krotki

if len(inventory) <= 1:
    print("\nTwoj dobytek zawiera", len(inventory), "element")
else:
    print("\nTwoj dobytek zawiera", len(inventory), "elementy")

# sprawdzenie czy eleement nalezy do krotki za pomoca operatora in

if "gumijagody" in inventory:
    print("Dożyjesz dnia w którym zatanczysz solówkę")
else:
    print("Będzie oklep")


# wyświetl jeden elemnt wskazany przez indeks

index = int(input("\nWprowadź index elementu inwentarza: "))
print("Pod indeksem", index, "znajduje sie", inventory[index])

#wyświetl wycinek
start = int(input("\nWprowadź indeks wyznaczający początek wycinka: "))
finish = int(input("\nWprowadź indeks wyznaczający koniec wycinka: "))
print("inventory[", start, ":", finish, "] to", end=" ")
print(inventory[start:finish])

input("\nAby kontynuować grę, naciśnij klawisz Enter.")

# dokonaj konkatenacji dwóch krotek
chest = ("złoto", "klejnoty")
print("Znajdujesz skrzynię, która zawiera:")
print(chest)
print("Dodajesz zawartość skrzyni do swojego inwentarza.")
inventory += chest
print("Twój aktualny inwentarz to:")
print(inventory)

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
