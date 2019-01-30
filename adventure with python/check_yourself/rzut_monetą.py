# napisz program który "rzuca" 100 ray monetą, a nastęþnie podaje użytownikowi liczbę orzełków i reszek

import random

eagle = 0
tails = 0
count = 0

while True:
    count += 1
    losowanie = random.randint(1, 2)
    if count > 100:
        break
    elif losowanie % 2 == 0:
        eagle += 1
        # print (eagle)
    else:
        tails += 1
        # print(tails)
 
 
print("Po stukrotnym rzucie monetą otrzymałeś nstepujace wyniki: ")
print("Orzeł wypadł: ", eagle , " razy.")
print("Rreszka wypadła: ", tails, " razy.")

input("\n\n\t\tAby zakonczyć program, nacisnij klawisz enter")        