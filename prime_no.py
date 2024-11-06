def prime_no(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        return True 
        
list_prime=list(filter(lambda x: prime_no(x),range(21)))
for i in range(21):
    if prime_no(i):
        list_prime.append(i)
        
print(list_prime)

        