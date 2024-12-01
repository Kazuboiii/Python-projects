def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "house_num" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('house_num')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')},{kwargs.get('state')}")


shipping_label("MR.","Spongebob","Squarepants",
               street="Pineapple st.",
               house_num="",
               city="Underwater",
               state="ocean")