killer={
    "krishna":'kans',
    "ram":'ravan',
    "bheem":'duryodhan',
    'arjun':'karn',
    'arjun':'jayadratha',
    'bheem':['duryodhan','dushasan','vikarna','kauravas']
}

print(killer)

print(killer['arjun'])

print(killer['ram'])

print(killer['arjun'])

print(len(killer))

print(killer['bheem'])

print(type(killer))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

ravan=killer.get('ram')
print(ravan)

surname_name={
    "Dabhi":'Arjun',
    "Joshi":'Dev',
    "Gop":"Anand",
    "Priya":"bharat",
}

print(surname_name.get('Priya'))

print(surname_name.keys())

print(surname_name.values())

surname_name['Dabhi']="Gopi"
print(surname_name)

x=surname_name.items()

print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)





