krotka = (1,2,3,4)

print(krotka)

# dictionary - słownik KLUCZ WARTOŚĆ

pokoje = {49: 'Karol M',
          69: 'Beta Z',
          10: 'Janina J'}
print(pokoje[49])

pokoje[49] = 'Stefan S'

print(pokoje[49])

pokoje[50] = 'Barbara BB'

print(pokoje)

# update dodaje
pokoje.update({999: 'Emila P'})
print(pokoje)

# del usuwa
del(pokoje[49])
print(pokoje)