# Python has no command for declaring a variable.

# A variable is created the moment you first assign a value to it

i=10
q="Name"
print(i)
print(q)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.

z=5
z=True
print(z)

# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


print(x,y,z)

# You can get the data type of a variable with the type() function.

t=15
print(type(t))

t=True
print(type(t))

# String variables can be declared either by using single or double quotes:

name="Arjun"
surname='Chandravanshi'
print(name, surname)

# Variable names are case-sensitive.

x=15
X=30
print(x,X)

# both are different



# 👻👻👻 Variable Names 👻👻👻

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

variable=5
_variable=5
variable_=5
Var=5
vAr=5
VAr=5

x,y,x="Orange",'banana','am'
print(x,y,z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "awesome"

# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)