#VARIABLE SCOPE = Where a variable is visible and accessible
#SCOPE RESOLUTION = (LEGB) Local-> Enclosed -> Global -> Built-in

def func1():
    print(x)

def func2():
    print(x)

x = 3

func1()
func2()