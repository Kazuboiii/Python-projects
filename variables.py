#Variables are a container for a value(String,integer,float,boolean) and are reuseable
# a variable behaves as if it was the value it contains

#Strings
First_name="kazuboiiiiiii"
Food="egg fried rice"
Email="kazuboiiii123@gmail.com"
print(f"hello {First_name} ")
print(f"you like {Food}")
print(f"your email is {Email} ")

#integers
age=20
number_of_students=30
Class=10
print(f"you are {age} years old")
print(f"there are {number_of_students} in your class")
print(f"you study in grade{Class}")

#float
price=19.99
Weight=25.6
GPA=3.59
Distance=5.5
print(f"the price of this box is {price}")
print(f"the weight of this box is {Weight} Kg")
print(f"your Gpa is {GPA}")
print(f"you ran {Distance} Km")

#Boolean
is_student=True
print(f'are you a student? {is_student}')

for_sale=False
if is_student:
    print("you are a student")
else:
    print("you are not a student")
if for_sale:
    print("that item is for sale")
else:
    print("that item is not for sale")
