
temperature=float(input("enter the temperature: "))
unit=input("enter the unit it is in(C or F or K)")

if unit=="C":
    conversion=input("what do you want the conversion in?")
    if conversion=="F":
        Fahrenheit= temperature *9/5+32
        print(f"The conversion to Fahrenheit is {round(Fahrenheit,2)}°f")
    elif conversion =="K":
       Kelvin= temperature+273.15
       print(f"The conversion to Kelvin is {round(Kelvin,2)}°k")
    else:
      print("please enver a valid valid unit for conversion!!")

elif unit=="F":
    conversion = input("what do you want the conversion in?")
    if conversion == "C":
      Celsius = (temperature - 32) * 5 / 9
      print(f"The conversion to Celsius is {round(Celsius, 2)}°c")
    elif conversion == "K":
       Kelvin = temperature + 459.67 *5/9
       print(f"The conversion to Kelvin is {round(Kelvin, 2)}°k")
    else:
       print("please enver a valid valid unit for conversion!!")

elif unit=="K":
    conversion = input("what do you want the conversion in?")
    if conversion=="F":
       Fahrenheit= (temperature-273.15)* 1.8 + 32
       print(f"The conversion to Fahrenheit is {round(Fahrenheit,2)}°f")
    elif conversion=="C":
        Celsius = temperature-273.15
        print(f"The conversion to Celsius is {round(Celsius, 2)}°c")
    else:
       print("enter a valid unit fo9r conversion")

else:
   print("enter a valid unit for your temperature")
