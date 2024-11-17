# input_val=a1b10
# output=abbbbbbbbbb

def string_val(input_val):
    output = ""
    temp_char = ""
    temp_num = ""
    
    for char in input_val:
        if char.isalpha():
            if temp_char and temp_num:
                output += temp_char * int(temp_num)
                temp_num = ""
            temp_char = char
        elif char.isdigit():
            temp_num += char
    
    if temp_char and temp_num:
        output += temp_char * int(temp_num)
    
    return output
    
input_val=input("Enter the Input:  ")
print(string_val(input_val))

