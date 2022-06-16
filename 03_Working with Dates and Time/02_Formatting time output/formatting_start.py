from datetime import datetime

def main():
    now = datetime.now()

    # THESE ALL ARE STORED IN datetime module
    ### DATE FORMATTING ###
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current Year is: %Y"))
    print(now.strftime("%a, %d, %B, %y"))

    # %c - locale's date and time , %x - locale's date , %X - locale's time
    print(now.strftime("Local date and time: %c"))
    print(now.strftime("Local date: %x"))
    print(now.strftime("Local time: %X"))

    ### TIME FORMATING ###
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I:%M:%S %p"))
    print(now.strftime("24-Hour time: %H:%M"))

if __name__ == "__main__":
    main();