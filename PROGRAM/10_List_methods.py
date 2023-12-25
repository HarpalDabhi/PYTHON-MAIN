countries_of_akhand_bharat = [
    "India",
    "Pakistan",
    "Bangladesh",
    "Nepal",
    "Bhutan",
    "Sri Lanka",
    "Afghanistan",
    "Maldives",
    "Myanmar",
]

print(countries_of_akhand_bharat)

print(len(countries_of_akhand_bharat))

all=countries_of_akhand_bharat*2
print(all)

alphabets=[]

uppercase_alphabet = [chr(x) for x in range(65, 91)]

print(uppercase_alphabet)

print(uppercase_alphabet[-1])

print(uppercase_alphabet[10])

print(uppercase_alphabet.index('H'))
print(uppercase_alphabet.index('A'))

print(len(uppercase_alphabet))

print(uppercase_alphabet[1:12])
print(uppercase_alphabet[-11:-3])

rev=uppercase_alphabet.reverse()

rev=uppercase_alphabet[::-1]
print(uppercase_alphabet[5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[4:])

thislist[0]="Apple"

print(thislist)

thislist[1:4]=["Melon"]
print(thislist)

thislist.insert(1,"Jamboo")

print(thislist)

friends=["Malay"]

friends.append("Elesh")
friends.append("Harpal")
print(friends)

friends.insert(1,"Ram")
print(friends)

mahabhrat=["Arjun","Bheem","Sahdev"]

ramayan=["Laxman","Ram","Shatrughna"]

mahabhrat.extend(ramayan)

print(mahabhrat)

mahabhrat.insert(0,"Udhisthir")
mahabhrat.append("Bharat")

mahabhrat.insert(-1,"Nakul")
print(mahabhrat)

# Remove Items

mahabhrat.remove("Bheem")
print(mahabhrat)

mahabhrat.pop(0)
mahabhrat.pop(0)
print(mahabhrat.pop(0))
print(mahabhrat)

ramayan=mahabhrat
print(ramayan)

del ramayan[2]
del ramayan[2]

ramayan.clear()

del ramayan

print(mahabhrat)

for friend in friends:
    print(friend)
else:
    print("End \n")

[print(x) for x in friends]

numbers=[1,5,6,7,8,11,5,6]
booleans=[True,False,True,True]

numbers.sort(reverse=True)
print(numbers)

nums=numbers.copy()

x=[1,4,9,16]
y=x.copy()
z=x

print(x)
print(y)
print(z)

z.append(25)
z.append(36)

print(z)

z.sort(reverse=True)

print(z)

z.remove(25)
z.pop()

print(z)

print(z.count(9))

print(z)

print(z.index(4))

x=[]
print(len(x))

