
import random
def random_value():
    return(a,b)
a=random.randrange(0,100)
b=random.randrange(0,100)
result = a * b
while True:
    print('How much is',a,"times",b)
    input=int(input())
    if input==result:
        print('done')
    break
else:
    print(a," times",b,"is not", result, "please try again: ")
    continue