import random

x=random.randint(1,100)
y=random.randint(1,100-x or 10)
z=100-x-y

print(x,y,z)

print(x+y+z)

print(5 and 10)

random_num_li=[]

for i in range(11):
    o=random.randint(10,99)
    random_num_li.append(o)

print(random_num_li)

print(min(random_num_li))
print(max(random_num_li))

