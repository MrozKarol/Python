import sys
evenNumbers = [element
                for element in range(400)
                if (element % 2 == 0)
                ]

print (evenNumbers)

evenNumbersGenerator = (element
                        for element in range(400)
                        if (element % 2 == 0)
                       )
# for irem in evenNumbersGenerator:
#     print(irem)                       

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumbersGenerator))