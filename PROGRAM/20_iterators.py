mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print(type(myit))

for i in myit:
    print(i)
else:
    print("End")

stringName="Akhand Bharata\n"
strit=iter(stringName)

strN="\n\nA"
print(len(strN))

for i in strN:
    print(i)

for i in stringName:
    print(next(strit))