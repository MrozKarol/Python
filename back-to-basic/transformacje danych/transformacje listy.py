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

# wyrazenie listowne przykład :
potegiDwojki2 = [element**2 for element in liczbyParzyste]

print(potegiDwojki)

# wyrazenie listowne przykład2 z uzyciem enter zeby kod był lepiej czytelny :

liczbyParzyste2 = [element
                    for element in liczby
                    if(element %2 == 0)
                    ]
print(liczbyParzyste2)  

"""
[co_zrobic_na_elemencie | for element in stara_lista | warunek_oparty_na_elemencie]
"""