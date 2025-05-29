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

def get_timestanmp(date):
    return date.timestamp()

print(get_timestanmp(datetime.now()))

future_date = datetime.now() + timedelta(days=30)
print(future_date)

init_date = datetime(2024, 3, 15)
new_date = init_date + timedelta(days=30)
print(new_date)

date1 = datetime(2023, 6, 1)
date2 = datetime(2024, 1, 1)

if date1 < date2:
    print("date1 es anterior")
else:
    print("date2 es anterior")

dates = [datetime(2022, 5, 1), datetime(2020, 1, 15), datetime(2023, 12, 31)]
sorted_dates = sorted(dates)

for f in sorted_dates:
    print(f)

current_time = time(21, 6, 0)
print(current_time.hour)








