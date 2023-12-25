try:
    print(x)
except NameError:
    print("Name Error")
finally:
    print("Code Executed")


y=input("Enter Number")

try:
    print(10+y)
except TypeError:
    print("Type Error")
finally:
    print("Code Executed")

li=[0,4,5]

try:
    print(li[4])
except IndexError:
    print("Index Error")
finally:
    print("Finally Executed")

