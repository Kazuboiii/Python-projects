# *args    =allows you to pass multiple non-key arguments // tuple
# **kwargs = allows you to pass multiple keyword-arguments // dictionaries
#           * unpacking operator

#def add(*args):
#    total=0
#    for arg in args:
#       total += arg
#    return total

#print(add(1,2,3))

#def display_name(*names):
#    for name in names:
#        print(name,end=" ")

#display_name("mr","sunisha","bhattarai")

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:10}: {value}")

print_address(house_num="22",
              street="siddhartha marg 123",
              city="kathmandu",
              province="bagmati")