import shelve
from datetime import datetime

d = datetime.now()

ids = 4

date , hour ,minute  = d.day, d.hour, d.minute

print("date :", d.day)
print("hour :" , d.hour)
print("minute :" , d.minute)


if date % 2 == 0 and hour == 00 and minute <= 15:

    s = shelve.open("test")
    s['ids'] = 45
    s.close()


p = shelve.open('test')
if 'ids' not in p:
    print("hello")
else:
    ids = p['ids']
p.close()


print("id is : " , ids, )
