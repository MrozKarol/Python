# wymieszane litery
# komputer wybiera losowo słowo a potem miesza w nim litery
# gracz powinien odgadnąć w niem pierwotne słowo

import random

# utworzenie specjalnej zmiennej i przypisanie jej krotki

WORDS = ("python", "javascript", "git", "konglomerat", "odpowiedź")

# wybierz losowo jedno słowo z sekwencji

word = random.choice(WORDS)

print(word)

#utwórz zmienną by później uzyć jej do sprawdzenia czy odpowiedź jest poprawna
correct = word

# utzótz zmienna do której przypiszesz pomieszana wersje słowa
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word = word[:position] + word[(position + 1):]

print(jumble)
