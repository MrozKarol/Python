# Bez samogłosek
# Demonstruje tworzenie nowych łańcuchów przy użyciu pętli for

message = input("Wprowadź komunikat: ")
new_message = ""
new_message0 = ""
VOWELS = "aąeęioóuy"

print()
for janusz in message:
    if janusz.lower() not in VOWELS:
        new_message += janusz
        print("Został utworzony nowy łańcuch: ", new_message)

print()
for janusz in message:
    if janusz.lower() in VOWELS:
        new_message0 += janusz
        print("Został utworzony nowy łańcuch gó: ", new_message)        
    


print("\nTwój komunikat bez samogłosek to:", new_message,)
print("\nTwój komunikat z samogłosek to:", new_message0,)    

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")