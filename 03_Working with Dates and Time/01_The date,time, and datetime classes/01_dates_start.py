# THE DATE, TIME, AND DATETIME CLASSES
from datetime import date
from datetime import time
from datetime import datetime

def main():
    # DATE OBJECTS
    today = date.today()
    print("Today's date is",today)

    print("Date components:",today.day, today.month, today.year)

    print("Today's weekday # is", today.weekday())

    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Which is a:", days[today.weekday()])

    # now working with DATETIME OBJECTS
    today1 = datetime.now()
    print("The current date and time is", today1)

    t = datetime.time(datetime.now())
    print(t)

if __name__ == "__main__":
    main();