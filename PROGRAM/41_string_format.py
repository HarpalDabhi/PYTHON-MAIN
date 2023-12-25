letter="My name is {} and I am from {}"
name="Harpal"
country="Bharat"

print(letter.format(name, country))

mahabharat=" In {2} {1} killed {3} at his {0} age."
age=16
hero="Krishna"
dead="Kans"
where="Mahabharat"

print(mahabharat.format(age, hero, where,dead))

movie="KGF Chapter 2"
earn=1235

print(f" {movie} has earned {earn} crore.")

import math
x=math.sqrt(2)

print(f" Price {x:.3f}")