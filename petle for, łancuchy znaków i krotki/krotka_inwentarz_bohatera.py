# Demonstruje tworzenie krotek
# inwentarz bochatera

# utwurz pustą krotkę

inventory = ()

# traktowanie krotki jako warunek
if not inventory:
    print("Nie posiadasz nieczego")

input("\nAby kontynować misje naciśnij Enter")

inventory =("miecz zagłady","wypasiona zbroja","tarcza szmato","gumijagody")

# wyświtl krotke
print("\nWykaz zawartości krotki")
print(inventory)

# wyświtl każdy elemnt ktroki
print("\nElementy wyposażenia:")
for item in inventory:
    print(item.upper())

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")