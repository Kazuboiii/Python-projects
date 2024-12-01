#FORMAT SPECIFIER= {:flags} format a value based on what flags are inserted

#.(number)f= round to that many decimal places (fixed point)
#:(number)=allocate that many spaces
#:03= allocate and zero pad that many spaces
#:<=Left justify
#:>=right justify
#:^=center align
#:+= use a plus sign to indicate positive value
#:= =place a sign to leftmost position
#: =insert a space before positive numbers
#:,=comma seperator

price1=21939.2234
price2=-3493939.2223
price3=974374.122
print(f"price 1 is {price1:+,.2f}")
print(f"price 1 is {price2:+,.2f}")
print(f"price 1 is {price3:+,.2f}")
