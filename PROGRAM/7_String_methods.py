hello="Hello, World "
Hello='Hello,World with Single Quotes'

print(hello+Hello)

indexedStr="MAHABHARAT"
#Accessing characters using index
print(indexedStr[0])

print(indexedStr[1:6])

print(indexedStr[::-1])

for i in indexedStr:
    print(i,end="  ")
else:
    print("End")

print("HA" in indexedStr)

print(len(indexedStr))

if "H" in indexedStr:
    print("Yes")


# Slice str
    
x="Hello Friends, I am Google Assistant"

print(x[2:10])

print(x[12:])

z="123456789"
print(z[-8:-2])

ram='RamaYan'

print(ram.upper())
print(ram.lower())
print(ram.capitalize())

str_strip="             Hello,      World                           "
print(str_strip)
print(str_strip.strip())

print(ram.replace("R","D").capitalize())

print(ram.split('a'))

# Contacte
name="Krishna"
whom="Radha"

print(name+" "+"love"+" "+whom)

love="{} loves {} too much"
print(love.format(name,whom))

khanva_war="""
The Battle of Khanwa, fought on March 16, 1527, was a pivotal clash between the Mughal forces of Babur and the Rajput Confederacy led by Rana Sanga for control of northern India. It was a brutal and decisive battle that shaped the course of Indian history."""

print(khanva_war)

print(khanva_war.capitalize())

print(khanva_war.casefold())

pratap="maharan Pratap"

print("\n\n")

print(pratap.capitalize())
print(pratap.casefold())
print(pratap.lower())
print(pratap.count('a'))

x=bool(False)
y=bool(None)
a=bool(0)
b=bool("")
c=bool(())
d=bool([])
e=bool({})

print(a,b,c,d,e,x,y)