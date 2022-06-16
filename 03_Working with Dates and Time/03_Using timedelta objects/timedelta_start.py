from datetime import date
from datetime import time
from datetime import datetime 
from datetime import timedelta

# timedelta is not a specific date or time, its a span of time and this class can be used to perform time-based mathematic

print(timedelta(days=365, hours=5, minutes=1)) # construct a basic timedelta and print it

# print today's date
now = datetime.now()
print("today is: " + str(now))

# print today's date one year from now
print("One year from now today will be: " + str(now + timedelta(days=365)))

# create timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be " + str(now + timedelta(days=2, weeks=3))) 
# so with timedelta we can calculate date time etc in advance or future

# now calculate for past
# calculate the date 1 week ago, formatted as a string 
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("One week ago was: " + s)

## How many days until next April Fools' day?
today = date.today()
afd = date(today.year, 4, 1)
# now use date comparison to see if April Fools' has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today: # we have use normal comparison operator
    print("April Fools' day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year + 1)

# now calculate the amount of time until next April Fools' day
time_to_afd = afd-today
print("It's just ", time_to_afd.days, "days until April Fools' day")