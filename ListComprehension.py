# get input from the user even num b/w 1and user input - lsit comp

user_input=int(input("enter the number "))

list_comp = [i for i in range(1,user_input-1) if i%2==0]
print(list_comp) 