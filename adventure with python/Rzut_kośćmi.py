#Rzut kośćmi
import random
die1 = random.randint(1,6) #losuje z przedziału od 1 do 6
die2 = random.randrange(6) + 1 # losuje od 0 do 5 dlatego plus 1 
total = die1 + die2

print("Wyrzuciłeś liczbe ", die1, "oraz ", die2, "i uzyskałeś sumę: ", "\n\t\t", total)

input("\n\n\t\tAby zakonczyć program, nacisnij klawisz enter")