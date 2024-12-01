#MODULE = a file containing code you want to include in your program
#        use 'import' to include a module (built-in or your own)
#        useful to break up a large program reusable separate files

#import math
#import math as m
#from math import e
#a,b,c,d,e=(1,2,3,4,5)
#print(math.e **a)
#print(math.e**b)
#print(math.e**c)
#print(math.e**d)
#print(math.e**e)

import example100

result=example100.pi
result1=example100.square(3)
result2=example100.cube(3)
result3=example100.circumference(3)
result4=example100.area(3)

print(result,result1,result2,result3,result4)