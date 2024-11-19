menu={"popcorn": 400,
      "cheese popcorn": 550,
      "chips": 80,
      "sweet corn": 350,
      "fries": 200,
      "cola": 150,
      "fanta": 150,
      "mountain dew": 150,
      "pizza": 900,
      "water": 18}

cart=[]
total=0
print("--------- MENU ---------")
for key,value in menu.items():
    print(f"{key:25}:RS.{value:.2f}")
print("------------------------")

while True:
    food=input('Enter the item you want to buy(press q to exit): ').lower()
    if food =='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------- YOUR ORDER -------------")
for food in cart:
    total+= menu.get(food)
    print(food.upper(),end=" ")

print()
print(f"The Total price for your items is Rs.{total:.2f}")