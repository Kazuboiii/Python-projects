#Collection= Single "variable" used to store multiple values
# List= [] ordered and changeable. Duplicates OK
# SET= {} unordered and immutable, but add/ removes OK.NO duplicates
# Tuple= () ordered and unchangeable.Duplicates Ok.Faster
#Exercise= shopping cart program!!!


fruits=[]
prices=[]
total=0
while True:
    fruit=input("Enter the fruits you want (Press e to quit):")
    if fruit.lower()=="e":
      break
    else:
      price=float(input(f"enter the prices of a {fruit} is:$"))
      fruits.append(fruit)
      prices.append(price)

print("Your Items are!!!")
for fruit in fruits:
    print(fruit,end=" ")

for price in prices:
    total=total+price

print()
print(f"Your Total price is ${total:.2f}")