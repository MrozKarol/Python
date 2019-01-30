# napisz program który "rzuca" 100 ray monetą, a nastęþnie podaje użytownikowi liczbę orzełków i reszek

import random

range_of_numbers = random.randint(1,100)



if range_of_numbers % 2 == 0:
    print("orzeł")
else:
    print("reszka")

input("\n\n\t\tAby zakonczyć program, nacisnij klawisz enter")        