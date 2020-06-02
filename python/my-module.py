import string_utilitie

print(string_utilitie.reverse_words("Yes No"))


import random
print(random.randint(1,10))
print(random.choice(["Rock","paper","Scissors"]))

import uuid
print(uuid.uuid1())
print(uuid.uuid4())
print(str(uuid.uuid4()))


import datetime
today=datetime.date.today()
print(today)

print(today.day, today.month, today.year)

d=datetime.date(2020, 2, 2)
print(d)
print(d.weekday())


print(d.strftime("%d-%m-%Y"))
print(d.strftime("%d-%b-%Y"))

now=datetime.datetime.now()
print(now)

if __name__=="__main__":
    import sys
    print(sys.argv)