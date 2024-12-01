#Default Arguments= A default value for the certain parameters
#                   default is used when that argument is omitted
#                   make your functions more flexible, reduces # of argument
#                   !. positional, 2. Default, 3. Keyword, 4. Arbitrary

#def shop(price,tax,discount=0.02):
#    return price * (1 - discount) * (1+tax)

#print(shop(500,0.05))

import time

def count(start,end=0):
    for x in range(start,end-1,-1):
        print(x)
        time.sleep(1)
    print("DONE!!!")

count(10)