sqr=lambda x:x*x
print(sqr(45))

for i in range(1,11):
    print(sqr(i))
else:
    print("End\n")

feranhit=lambda c:(9/5)*c+32

celcius=lambda f:5/9*(f-32)

print(feranhit(100))
print(celcius(10))

choice=input("F = Convert into feranhit . C= Convert into Celcius. \n : ")

choice=choice.upper()

if choice=="F":
    temp=float(input("Enter temperature :"))
    print(feranhit(temp))
elif choice=="C":
    temp=float(input("Enter temperature :"))
    print(celcius(temp))

