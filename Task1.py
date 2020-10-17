#Write a Boolean function named is_prime which takes an integer as an argument and returns true if the argument is a prime number, or false otherwise. 
import random
def is_prime(n):
    if (n>1):
        for i in range(2,n):
            if(n % i==0):
                return False
            else:
                    return True        
#Then write a program that generates six random number between 1 and 100 (inclusive) and print out the result like the following (each run will have six different random numbers):
import random
for i in range(1,7):
    n=random.randrange(1,101)
    is_prime(n)
    if is_prime(n)==True:
        print('The random number',n,'is prime number')
    elif is_prime(n)==False:
            print('The random number',n,'is not a prime number')