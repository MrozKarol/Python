# Dostęp swobodny
# Prezentuje indeksowanie łańcucha znaków

import random

word = input("Wprowadź komunikat:")


print("WArtość zmiennej word to: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(20):
    position = random.randrange(low, high)
    print("word[",position, "]\t", word[position])

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")      
