# break

wynik = 0 

for i in range(0,3):
    x = int(input('Podaj dodatnią liczbę'))
    if(x>0):
        wynik += x
        print(wynik)
    else:
        print('Miała być liczba dodatnia')    
        break
    print('Aktualny wynik dodawania to :', wynik)
        
    

