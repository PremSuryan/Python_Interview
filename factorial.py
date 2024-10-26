"""
Recursion function --> function calling function to do task EG: Factorial
"""

def factorial(n):
    if n<0:
        raise ValueError("Factorial is not defined for negative numbers.")
        
    elif n==0 or n==1:
        return 1
        
    else:
        return n * factorial(n-1)
        
print(factorial(5))