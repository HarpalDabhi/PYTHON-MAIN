def func():
    global x
    x=10
    print(x)

func()

print(x)

global y


def func2():
    y=200
    print(y)

func2()
print(y)