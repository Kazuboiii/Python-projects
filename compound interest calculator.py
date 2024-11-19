principle=0
time=0
rate=0

while principle<=0:
    principle = float(input("enter the principle amount:"))
    if principle<=0:
        print("principle cannot be less than or equal to zero")

while time<=0:
    time = int(input("Enter the time period for the amount in years:"))
    if time <= 0:
        print("time cannot be less than or equal to zero")

while rate<=0:
    rate = float(input("enter the interest rate for the amount:"))
    if rate <= 0:
        print("Rate cannot be less than or equal to zero")

total=principle*pow((1+rate/100),time)
print(f"the total compound interest after {time} year/s: Rs.{total:.2f}")