name=input("enter your username:")

if len(name)>12:
    print("you cannot have a username containing more than 12 characters!!! ")
elif not name.find(" ")==-1:
    print("Username cannot contain Spaces:")
elif not name.isalpha():
    print("Username cannot contain digits")
else:
    print(F"welcome {name}")


