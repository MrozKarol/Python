# break

wynik = 0 
i = 0
while i < 3:
    x = int(input('Podaj dodatnią liczbę'))
    if(x>0):
        wynik += x
        print(wynik)
    else:
        print('Miała być liczba dodatnia')    
        # break
        continue
    print('Aktualny wynik dodawania to :', wynik)
    i +=1    
    

