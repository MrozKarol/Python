# petla

# number =  int(input('Wpisz liczbę która zmniejszy sie do 0: '))

# while number >= 0:
#     print(number)
#     number -=1

# ćwiczenie jeden: program pyta ile chcesz zsumować ze sobą liczb

wynik = 0
i = 0

xSum = int((input('podaj ile chcesz zsumować ze sobą liczb: ')))

while i < xSum:
    x = int(input('Podaj liczbę: '))
    wynik += x
    i += 1

print("Wynik dodawania liczn to:", wynik)   