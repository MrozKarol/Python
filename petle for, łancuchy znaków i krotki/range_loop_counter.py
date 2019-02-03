# Licznik
# Demonstruje funkcje range(), do liczenia na wszelkie mozliwe sposoby w połaczeniu z pętlą for

print("Liczenie do przedu:")
for i in range(10):
    print (i, end=" ")


print("\n\nLiczenie co pięć:")
for i in range(0, 50, 5): #z trzema argumentami, zostana one potraktowane jako punkt początkowy, punkt koncowy i liczba wskazujaca co ile nazlezy liczyć
    print(i, end=" ")


print("\n\nLiczenie od tyłu")
for i in range(20, 0, -2):
    print(i, end=" ")   


