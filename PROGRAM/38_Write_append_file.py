def WriteTable(x):   
    file=open("table.txt",'w')
    file.write(f"Table {x}")
    file.write(f"\n")
    for i in range(1,11):
        file.write(f"{x} X {i} = {x*i}")
        if i<10:
            file.write(f"\n")
    file.close()

# WriteTable(16)
    
import datetime
t=datetime.datetime.now()
tm=t.strftime("%H:%M:%S")
print(tm)

dt=t.strftime("%A, %d %B %Y")
print(dt)

def AppendCommit():
    f=open('Commit.txt', 'a')
    f.write(f"{dt}    :      {tm}")
    f.write("\n")
    messege=input("Enter commit  : ")
    f.write(f"Your Message => \n {messege}")
    f.write("\n________________________________\n")
    f.close()

AppendCommit()