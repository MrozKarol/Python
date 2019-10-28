# wynik = 0

# for i in range(0,200):
#    if( i % 2 == 0):
#        print('Liczba', i, 'jest parzysta')

# print("Wynik dodawania liczb to:", wynik)    

# wypisz liczby od 0 do 200 które są podzielne przez 5 i nie są podzielne przez 7

print('Program wypisje liczny liczby od 0 do 200 które są podzielne przez 5 i nie są podzielne przez 7 ')

for i in range(0,201):
    if( i % 5 == 0):
        print('Liczby podzielne przez 5 to:', i)  
    elif(not(i % 7 == 0)):
        print('Liczby które nie są podzielne przez 7 to:', i)  