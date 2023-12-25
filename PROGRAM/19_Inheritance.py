class Animal:
    def __init__(self,hero,villain):
        self.hero=hero
        self.villain=villain
    def printInfo(self):
        print(f"Animal movie has character hero is {self.hero} and villain is {self.villain}")

A=Animal("Ranvijay Singh","Abrar")

A.printInfo()

print("____________\n")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def PrintBio(self):
        print(f"{self.name} is {self.age} Years Old Person.")

P1=Person("Krishna",16)
P1.PrintBio()

class Student(Person):
    pass

S1=Student("Ram",14)
S1.PrintBio()

class CollegeStudent(Person):
    def __init__(self, name, age,course):
        super().__init__(name, age)
        self.course=course

    def printCollege(self):
        print(f"{self.name} is studying in {self.course} at {self.age} Age.")

College_Student_1=CollegeStudent("Elesh",20,"ME")
College_Student_1.printCollege()



