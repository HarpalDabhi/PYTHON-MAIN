file=open('Class_Object_Definition.txt')
read_=file.read()

print(len(read_))
print(read_.count('h'))

words=read_.split(' ')

for w in words:
    if len(w)<3:
        print(w)

file.close()

