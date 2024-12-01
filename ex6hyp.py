import math

perpendicular=float(input("enter the perpendicular of the right angled triangle: "))
base=float(input("enter the base of the right angles triangle; "))
hypotneous=math.sqrt(pow(perpendicular,2)+pow(base,2))
print(f"the hypotneous of the triangle is {round (hypotneous,2)}cm")