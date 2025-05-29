from datetime import datetime, date, time, timedelta

now = datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)

christmas = datetime(2025, 12, 25)
print(christmas)

hour = time(14, 30, 15)
print(hour.hour)
print(hour.minute)
print(hour.second)

today = date.today()
print(today)
year_init = date(today.year+1,1,1)
print(year_init)
diff = year_init - today
print(diff.days)