class MyClass:
  x = 5

print(MyClass.x)

p1=MyClass()

print(p1.x)

class War:
  def __init__(self,win,lose):
    self.win=win
    self.lose=lose

w1=War("Bheem","Duryodhan")
print(w1.win)

w2=War("Krishna","Kans")
print(w2.lose)

class SnakeGame:
  def __init__(self,player,score,direction):
    self.playerName=player
    self.GameScore=score
    self.SnakeDirection=direction

p1=SnakeGame("Harpal",120,"Left")

print(p1.GameScore)
print(p1.playerName)
print(p1.SnakeDirection)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

class MovieCollection:
  def __init__(self,movie,collection):
    self.movie=movie
    self.collection=collection
  def __str__(self):
    return f"{self.movie} has earned {self.collection} Rs. (Crore)"
    
m1=MovieCollection("KGF Chpater 2",1235.2)
print(m1)

m2=MovieCollection("RRR",1236)
print(m2)

m3=MovieCollection("Bahubali 2",1810)
print(m3)

    