# Python's library provides a couple of useful utilities for working with calendars in both text and HTML formats. 

# import calendar module
import calendar # So this statement will import all of the various classes from the calendar module into my app. 

# create a plain text calendar and to do that we use the text calendar class
c = calendar.TextCalendar(calendar.SUNDAY) # sunday will be the first day
# c = calendar.TextCalendar(calendar.MONDAY) # it will change the parameter to monday
st = c.formatmonth(2017, 1, 0, 0) # so the format month method lets me format a particular month into a text string
print(st)

# create a HTML formatted calendar and use HTML format class
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2017, 1)
print(st) # it will print a table based calendar

# loop over the days of a month
# zeroes at start and end mean that the day of the week is in an overlapping month or another adjacent month
for i in c.itermonthdays(2017, 8):
    print(i) # two zeroes at start mean that sunday and monday of that week are belong to the month of july

# calendar module provides useful utilities for the given locale.
# such as the names of the days and months in both full and abbreviated form.
for name in calendar.month_name:
    print(name)

for name in calendar.day_name:
    print(name)

'''Calculate days based on a rule: For example, 
consider a team meeting on the first friday of every month.
To figure out what days that would be for each month,
we can use this script: '''
print("Team meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2018, m)
    weekone = cal[0]
    weektwo = cal[1]

    '''the first Friday of that month has to be somewhere within the first two weeks. 
    So I've got two local variables here, week one and week two,
    which I retrieve from this cal array that I got back. 
    I then just need to see which of the two weeks has the first Friday. So, to do that,
    I'm going to use the calendar's Friday constant to index into each of these array.'''
 
    if weekone[calendar.FRIDAY] != 0:  # = 0 means that friday lies in the previous month
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))