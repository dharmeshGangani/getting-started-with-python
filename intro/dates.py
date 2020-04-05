# To get current date time, we need to use datetime library
from datetime import datetime, timedelta

current_date = datetime.now();
print("today is " + str(current_date))


new_dt = input("enter date (dd/mm/yyyy): ")
new_date = datetime.strptime(new_dt, "%d/%m/%Y")

one_day = timedelta(days=1)
yesterday = new_date - one_day
print("new yesterday was: " + str(yesterday))

one_week = timedelta(weeks=1)
last_week = new_date - one_week
print("last week was: " + str(last_week))

# one_month = timedelta(month=1)
# last_month = new_date - one_month
# print("last month was: " + str(last_month))

print("Day: " + str(current_date.day))
print("Month: " + str(current_date.month))
print("year: " + str(current_date.year))
print()
print("Hour: " + str(current_date.hour))
print("Min: " + str(current_date.minute))
print("Sec: " + str(current_date.second))
print()

birthday = input("enter birthday (dd/mm/yyyy): ")
print("Birthday = " + birthday)

birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print("Birthday Date = " + str(birthday_date))
