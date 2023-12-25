import datetime

x=datetime.datetime.now()
print(datetime.datetime.now())

print(x.year)
print(x.month)
print(x.day)
print(x.date())

print(x.strftime('%A'))

y=datetime.datetime(2001,4,17)
print(y.strftime('%A'))

z=x.strftime('%S')
print(z)

z=int(z)



