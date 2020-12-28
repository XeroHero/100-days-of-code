# 
# Performing calculations with Time Delta Class
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Construct a basic time delta and print it
print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print("Today is : " + str(now))

print("One year from now, it will be: " + str(now + timedelta(days=365)))

# time delta with more than 1 argument
print("In 2 days and 3 weeks, it will be " + str (now + timedelta(days=2, weeks=3)))

# calculations in the past
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago, it was: " +s )

# How many days till April fool's


today = date.today()
afd = date(today.year, 4,1)
if (afd < today):
    print("April fool's day already went by by %d days ago" %((today-afd).days))
    afd = afd.replace(year=today.year+1)

    # now calculate time unitl next AFD
time_to_afd = afd-today
print("It's just ", time_to_afd.days, "days until AFD")