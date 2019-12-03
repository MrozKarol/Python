"""
Znajdź liczby fo 100 do 470 włacznie, które śą: podzielne przez 7 
ale nie są podzielne przez 5
"""

numbers = (
    number
    for number in range (100,471)
    if (number % 7 == 0 and number % 5 !=0)
    
)

for number in numbers:
    print(number)