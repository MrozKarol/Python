#!/usr/bin/env python
# Operatory logiczne

# and - '1'
# 1 i 1  -True
# 1 i 0 - False
# 0 i 1 - False
# 0 i 0 -False

'''
or - 'lub'
1 -1 True
1 -0 True
0 - 1 True
0 - 0 False

not - nie jest
'''
wartosc = int(input('Sprawdzę, czy liczba jest z zakresu od 1 do 10: '))

if (wartosc > 1 and wartosc < 10):
    print('Wartosć jest od 1 do 10')
else:
    print("Wartość jest spoza zakresu")    

a = 5
b = 2

if (a == 5 or b == 3):
    print("tak")