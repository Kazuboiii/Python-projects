#Dictionaries= A collection if {Key:Value} pairs
#              Ordered and changeable. NO duplicates.

capitals={"USA": "Washington D.C",
          "INDIA": "New Delhi",
          "CHINA": "Beijing",
          "RUSSIA":"Moscow"}

#print(dir(capitals))
#print(help(capitals)
#print(capitals.get("JAPAN"))

#if capitals.get("RUSSIA"):
#    print("That capital exists")
#else:
#   print("That capital doesn't exist")

capitals.update({"JAPAN": "Tokyo",
                 "NEPAL": "Kathmandu",
                 "CANADA": "Ottawa"})
#capitals.pop('RUSSIA')
#print(capitals.get("JAPAN"))
#print(capitals)
#keys=capitals.keys()
#for key in capitals.keys():
#    print(key)
#values=capitals.values()
#for value in capitals.values():
#    print(value)
items = capitals.items()
#print(items)
for key, value in capitals.items():
   print(f"{key}:{value}")