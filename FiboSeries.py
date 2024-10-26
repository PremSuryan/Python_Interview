# print("Hello World")

# Fibonnoci Series:

def fibo_numbr(user_input):
    
    if user_input == 0:
        return 0
    elif user_input ==1 or user_input ==2:
        return 1
    else :
        return fibo_numbr(user_input-1) + fibo_numbr(user_input-2)

try:
    user_input = int(input("Enter the number:"))
    output = fibo_numbr(user_input)
    print(output)

except :
    print("You have entered the non number value please enter the number")

    
