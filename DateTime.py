import datetime

t = datetime.time(5,25,1)
print(t)

print(datetime.time)
print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

today = datetime.date.today()
print(today)
today.timetuple()
print(today.day)

d1 = datetime.date(2015,3,11)
print(d1)
d2 = d1.replace(year=1990)
print(d2)
d1-d2
datetime.timedelta(9131)