# Analizator komunikatów
# Demonstruje funkcje len() i operator in 

message = input("Wprowadź komunkat:")
print("\nDługość komunikatu wynosi:", len(message)) #do funkcji len mozna przekazac dowolna sekwencje, a funkcja zwróci jej długość, długość sekwencji to liczba jej elementów/

print("\nNajcześćiej używana litera w języku polskim, 'a',")
if "a" in message: # operator in mozna użyć do sprawdzenia czy jakiś element jest składnikiem sekwencji, wystarczy po elemencie do zbadania umieścić operator in a po nim samą sekwencię. w ten sposób utworzysz warunek.
    print("wystąpiła w Twoim komunikacie.")
else:
    print("Nie wystąpiła w Twoim komunikacie")   

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
