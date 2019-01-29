# Komputer nastrojów
# Demonstruje klauzulę elif

import random

print("Wyczuwam Twoją energię. Twoje prawdziwe emocje znajdują odbicie na moim ekranie.")
print("Jak widzę")

mood = random.randint(0, 3)

if mood == 1:
    # szczęśliwy
    print( \
    """
        jezyk Python
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | .     . |
       |  `...`  |
       -----------
                   """)
elif mood == 2:
    # obojętny  
    print( \
    """
        inne jezyki
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       | ------  |
       |         |
       -----------
                   """)
elif mood == 3:
    # smutny
    print( \
    """
        jak widze JavaScript
       -----------
       |         |
       | O    O  |
       |   <     |
       |         |
       |  .'.    |
       | '   '   |
       -----------
                   """)
else:
    print("Nieprawidłowa wartość nastroju! (Musisz być naprawdę w złym humorze) pewnie CSS się rozjechały.")

print("...dzisiaj.")

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
