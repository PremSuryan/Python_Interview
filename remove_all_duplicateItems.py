list_value = [1,2,3,3,4,4,5]

duplicate_val=[]

for i in list_value:
    # for j in range(i+1):
        if i not in duplicate_val:
            duplicate_val.append(i) #None 
        else:
            duplicate_val.remove(i)

print(duplicate_val)  #output: [1,2,5]  