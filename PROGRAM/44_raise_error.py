def ValE():    
    x=int(input("Enter No :"))

    if x<0 or x>100:
        raise ValueError("Invalid")
    else:
        print("Success")

o=int(input("Enter :"))

if o=="Quit":
    raise print("Quit")
elif type(o)!=int:
    raise ValueError("Invalid")
else:
    print("Success")