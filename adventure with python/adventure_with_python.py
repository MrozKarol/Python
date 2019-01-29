#Maniulacje cytatami

quote ="Myślę ze jezyk programowania Python jest bardziej przemyślany niż JavaScrpt "
print("Moja opinia")
print(quote)

print("\nDużymi literami:")
print(quote.upper()) 

print("\nMałymi literami:")
print(quote.lower()) 

print("\nWszystkie wyrazy od duzej litery:")
print(quote.title()) 

print("\nZ dobrą zmianą:")
print(quote.replace("przemyślany", "zmyślny".upper()))

input("\n\n\t\tAby zakonczyć program, nacisnij klawisz enter")