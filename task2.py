#Create a function that randomly generates and returns a tuple of two positive one-digit integers. Then prompt the user for the multiplication of the two numbers. 
import random
def random_value():
    return(a,b)
a=random.randint(0,100)
b=random.randint(0,100)
result = a * b
while True:
    print('How much is',a,"times",b)
    user_value=int(input())
    if user_value==result:
        print('Done')
        exit(0)
    else:
        print(a," times",b,"is not", user_value, "Please try again!! ")
    continue
   