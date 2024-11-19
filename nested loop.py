#Nested Loop= A loop found inside another loop.
#              outer loop:
#                 inner loop:
#def star(n):
#   for x in range (1,n+1):
#    for y in range(n-x):
 #    print(" ",end="")

#    for k in range(1,x*2):
#      print("*",end="")
#
#    print()
#star(5)

rows=int(input("Enter the numbers of rows:"))
columns=int(input("Enter the number of columns:"))
symbol=input("enter the symbol you want to use:")
for x in range(rows):
    for y in range(columns):
        print(symbol,end="")

    print()