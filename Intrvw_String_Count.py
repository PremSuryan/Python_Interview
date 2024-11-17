"""
# input = "aapppak" 
# output = "a2p3a1k1"

"""


def compress_string(input_string):
    if not input_string:
        return ""
    
    result = []
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            result.append(input_string[i - 1] + str(count))
            count = 1

    # Append the last character and its count
    result.append(input_string[-1] + str(count))
    print(result)
    
    return ''.join(result)

# Example usage:
input_str = "aapppak"
output_str = compress_string(input_str)
print(output_str)  # Output: "a2p3a1k1"