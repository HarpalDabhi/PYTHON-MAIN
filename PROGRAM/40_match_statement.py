def sum(x,y):
    print(f"Sum {x+y}")

def sub(x,y):
    print(f"Sub {x-y}")

def mul(x,y):
    print(f"Mul {x*y}")

def div(x,y):
    print(f"Div {x/y}")

x=int(input("Enter Number : "))

o=15
p=7

match x:
    case 1:
        sum(o,p)
    case 2:
        sub(o,p)
    case 3:
        mul(o,p)
    case 4:
        div(o,p)
    case _:
        print("None")
