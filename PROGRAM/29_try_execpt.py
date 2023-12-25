try:
    print(x)
except:
    print("Failed to Print")

name="harpal"

try:
    for i in range(10):
        print(name[i])
except IndexError:
    print("Index Error")
finally:
    print("Block Completed")

try:
     print(2+"x")
except TypeError:
    print("Type Error")
finally:
    print("Block Completed")

