#
# Example for working with Calendars
#
import calendar
# # create plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
# st = c.formatmonth(2017, 1, 0, 0)
# print(st)

# create a HTML calendar

# hc = calendar.HTMLCalendar(calendar.MONDAY)
# st = hc.formatmonth(2021, 1)
# print(st)

# loop over the days of the month
# for i in c.itermonthdays(2020, 8):
    # print(i) # 0's here indicate weekdays that belong to another month

# using locales (get names local to the country the system is registered to)

# for name in calendar.month_name:
#     print(name)

# print()    
# for name in calendar.day_name:
#     print(name)

# calculate days based on a rule

print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2021, m)
    week_one = cal[0]
    week_two = cal[1]

    if week_one[calendar.FRIDAY != 0]:
        meetday = week_one[calendar.FRIDAY]

    else:
        meetday = week_two[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))