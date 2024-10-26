def is_palindrome(s):
    # Remove spaces and convert to lowercase
    # s = s.replace(" ", "").lower()
    # s = s.split().lower()

    s = ''.join(s.split()).lower()
    print(s)

    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
input_string = "A man a plan a canal Panama"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

"""
def palindrome(x):
    a = str(x)
    reverse_str = a[::-1]
    if a == reverse_str :
        return True
    else:
       return False 

x=121
print(palindrome(x))