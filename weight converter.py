# python weight converter

weight=float(input("enter the weight: "))
unit=input("The unit(K or L)")

if unit=="K":
    weight=weight*2.205
    print(f"weight is{round(weight,2)}lbs")
elif unit=="L":
    weight=weight/2.205
    print(f"the weight is{round(weight,2)}Kg")
else:
    print("please enter a valid unit as shown")

