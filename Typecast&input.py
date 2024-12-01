#Typecasting= The process of converting a variable from one data type to another
#               Str(),Int(),Float(),Bool()

name=""
age=25
gpa=3.2
is_student=True

name=bool(name)
print(name)
print(type(name))


# input()= A function that promotes the user to enter data, returns the data as a string

name=input("whaat is your name?")
age=int(input("how old are you??"))
age=age+1
print(f"hello {name}")
print("happy birthday!")
print(f"you are {age} years old")