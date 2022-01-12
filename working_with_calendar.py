import calendar

# Interesting way to print out entire calendar
# print(calendar.TextCalendar(firstweekday=7).formatyear(2022))

date_list = list(map(int, input().split()))

day_num = calendar.weekday(date_list[2], date_list[0], date_list[1])

day_name = calendar.day_name[day_num]

print(day_name.upper())
