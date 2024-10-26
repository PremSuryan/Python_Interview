"""
Remove Duplicate in the given list 
"""
list_value = [1,2,3,3,4,4,5]
remove_dupli = list(set(list_value))
print(remove_dupli)

"""
Remove Duplicate without Inbuild function
"""
list_value = [1, 2, 3, 3, 4, 4, 5]
unique_list = []

for item in list_value:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
