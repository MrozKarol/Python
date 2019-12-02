liczby = [1,2,3,4,5,6]

potegiDwojki =[]

for element in liczby:
    potegiDwojki.append(element**2)
print(potegiDwojki)


liczbyParzyste = []

for element in liczby:
    if(element %2 == 0):
        liczbyParzyste.append(element)
print(liczbyParzyste)        