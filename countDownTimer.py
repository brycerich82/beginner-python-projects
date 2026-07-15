import time

my_time = int(input("Enter the time in seconds: "))

SECONDS_IN_YEAR = 31536000
SECONDS_IN_WEEK = 604800
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

for x in range(my_time, 0, -1):
    years = int(x / SECONDS_IN_YEAR)
    remaining = x % SECONDS_IN_YEAR
    weeks = int(remaining / SECONDS_IN_WEEK)
    remaining = remaining % SECONDS_IN_WEEK
    days = int(remaining / SECONDS_IN_DAY)
    remaining = remaining % SECONDS_IN_DAY
    hours = int(remaining / SECONDS_IN_HOUR)
    remaining = remaining % SECONDS_IN_HOUR
    minutes = int(remaining / SECONDS_IN_MINUTE)
    seconds = remaining % SECONDS_IN_MINUTE
    print(f"{years:02}:{weeks:02}:{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")
