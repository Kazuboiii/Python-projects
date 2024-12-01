# exercise 2 shopping cart program

item=input("The item you want:")
price=float(input("the price for the item is :"))
quantity=int(input("the quantity you want:"))
total=price*quantity

print(f"the item is {item}")
print(f"The price is ${price}")
print(f"The quantity you brought is {quantity}")
print(f"Your total amount is ${total}")