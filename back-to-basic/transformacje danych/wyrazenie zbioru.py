"""
wyrażenie zbioru
"""
names = {'arkadiusz', "Wioletta", "karol", "bartłomiej", "Jakub", "Ania"}

names = {
    name.capitalize()
    for name in names
    if name[0] == 'a' or name[0] == "A"
}

print(names)