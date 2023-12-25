student_marks=[45,56,78,89,14,25]
index=0
for mark in student_marks:
    print(mark)
    if index==3:
        print("Aswesome")
    index+=1

print("________________________________________________________________\n")

for i,mark in enumerate(student_marks):
    print(mark)
    if i==3:
        print("Aswesome")
    index+=1

fruits=["Banana","Orange","Mango"]

for x in enumerate(fruits):
    print(list[x])