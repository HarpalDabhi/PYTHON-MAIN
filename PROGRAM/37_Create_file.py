def CreateFile():
   try:
       name=input("File Name :")
       file=open(f"{name}.txt",'+x')
   except IOError:
       print("Error opening file")
   finally:
       print("Created file")
 
# CreateFile()

def CreateFile2():
    try:
        name=input("Second File Name :")
        file=open(f"{name}.txt",'+x')
    except FileExistsError:
        print("File already exists")
    finally:
       print("Closing File")
       file.close()
 


CreateFile2()
  