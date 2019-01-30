#Ciastko z wróżbą, program powinien wyświetlić jedną z pięciu niepowtarzalnych przepownidni dokonując losowego wyboru

import random

omenNumber = random.randint(1,5)

omenOne = "Ziarnko do ziarnka zbierze się miarka."\
           + "Pamiętaj, aby gromadzić oszczędności –"\
           +"bez nich nie kupisz tego, o czym marzysz"

omenTwo = "Podróże małe i duże… w przyszłym roku" \
           +"koniecznie zainwestuj w walizkę. Przyda się jak nic innego."           

omenThree = "Pieniądze szczęścia nie dają,"\
            +" Ty przekonasz się, że tak nie jest. Czeka Cię wygrana!" 

omenFour = "Oj, postaraj się trochę bardziej – bez pracy nie ma kołaczy!"

omenFive = "W przyszłym roku powiększy Ci się rodzina! Gratulacje!"

omenNumber = 0


omenNumber = random.randint(1,5)



if omenNumber == 1:
    print("\n\tWróżba dnia:"+"\n\t"+ omenOne.upper())
elif omenNumber == 2:
    print("\n\tWróżba dnia:"+"\n\t"+ omenTwo.upper())
elif omenNumber == 3:
    print("\n\tWróżba dnia:"+"\n\t"+ omenThree.upper())
elif omenNumber == 4:
    print("\n\tWróżba dnia:"+"\n\t"+ omenFour.upper())
elif omenNumber == 5:
    print("\n\tWróżba dnia:"+"\n\t"+ omenFive.upper())        

else:
    print("Nie ma wróżby na dziś dla Ciebie przykro mi ")




input("\n\nAby zakończyć program wróżba dnia, naciśnij klawisz Enter.")