#!/usr/bin/env python
# spaw aby liczba ujemna stałą sie dodatnia


print('Program obliczna wartość bezwzgledna')

x = int(input('Podaj liczbę: '))

if(x < 0):
    print('Wartość bezwzgledna z ', str(x), 'to', str(x * -1))
elif (x > 0):
    print('Wartość bezwzgledna z ', str(x), 'to', str(x *  1))
elif (x == 0):
     print('Wartość bezwzgledna z ', str(x), 'to', str(x *  1))



