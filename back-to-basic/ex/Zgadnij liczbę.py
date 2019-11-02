# Program zgadnij liczbę 10 próbach

szukanaLiczba = 40

i = 0

while i < 10:
    x = int(input('Podaj liczbę : '))
    i += 1   
    print('Liczba prób', i)    
    if (x == szukanaLiczba):
        print("Brawo odnalzałeś liczbę !!! szukana liczba to", str(szukanaLiczba))
        break
    elif (i == 10):
            print("Nie udało Ci sie odgadnąć liczby przekroczyłeś maksymalną liczbę prób")
            wybor = str(input('naciśj a żeby zakończyć b żeby spróbować jeszcze raz'))
            if(wybor == 'a'):
                i = 0
                continue
            elif (wybor == 'b'):
                break
            print('Koniec programu')
    elif ((szukanaLiczba - x) < 5 and (x - szukanaLiczba)< 5):
            print('Jesteś blisko')
    elif ((szukanaLiczba - x) < 10 and (x - szukanaLiczba)< 10):
            print('Ooo ciepło to Twoj obszar poszukiwań')
    elif ((szukanaLiczba - x) < 20 and (x - szukanaLiczba)< 20):
            print('Nie jesteś nawet blisko')    
    # else:
    #     # if(i == 10):
    #     #     print("Nie udało Ci sie odgadnąć liczby przekroczyłeś maksymalną liczbę prób")
    #     #     wybor = str(input('naciśj a żeby zakończyć b żeby spróbować jeszcze raz'))
    #     #     if(wybor == 'a'):
    #     #         i = 0
    #     #         continue
    #     #     elif (wybor == 'b'):
    #     #         break
    #     #     print('Koniec programu')
    
     
        
        
    
