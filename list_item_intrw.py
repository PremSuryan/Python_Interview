"""
From a list of numbers , move zero to the end of the list
"""

list_numbers=[1,0,2,0,4,6]

for i in list_numbers:
    if i == 0:
        list_numbers.remove(i)
        list_numbers.append(i)

print(list_numbers)  