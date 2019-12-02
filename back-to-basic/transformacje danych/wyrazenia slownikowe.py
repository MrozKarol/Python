"""
    wyrażenie słownikowe
"""

names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

nameLength ={
    name : len(name)
    for name in names
    if name.startswith("A")
}

print(nameLength)

"""
przemnozenie razy 6
"""

mulitpledNumbers ={
    number : number * 6
    for number in numbers
}
print(mulitpledNumbers)

fahrebheit = {
    key: celcius*1.8+ 32
    for key, celcius in celcius.items()
}

print(fahrebheit)