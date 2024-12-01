#Functions = THEY ARE REUSABLE BLOCK OF CODE
#            PLACE () AFTER THE FUNCTION TO INVOKE IT

#def happy_birthday(name,age):
#    print(f"Happy Birthday {name}")
#    print(f"You are {age} years old")
#    print("Happy Birthday To YOU!!!!")
#   print()
#happy_birthday("steve",30)
#happy_birthday("Kazuha",20)

#Return= Statements use to end a function and send back the result to the caller

#def add(x,y):
#    z=x+y
 #   return z
#print(add(2,3))
def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+ last
full_name=create_name("kazuha","kaidehara")

print(f"Your name is  {full_name}")


