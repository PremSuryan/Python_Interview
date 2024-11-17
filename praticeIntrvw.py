name='pppreemm'
# Output=p3r1e2m2


def nameString(name):
    if not name:
        return 'No Input'

    empty_str=[]
    count=1

    for i in range(1,len(name)):
        if name[i] == name[i-1]:
            count+=1
        else :
            empty_str.append(name[i-1] + str(count))
            count=1

    empty_str.append(name[-1] + str(count))
    print(empty_str)

    return ''.join(empty_str)

            
output=print(nameString(name))

# result=nameString(name)
# print(result)