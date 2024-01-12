import datetime
import pytz

# today = datetime.date.today()
# # d = datetime.date(2016,7,24)
# # print(d)
# # print(today.year)
# # print(today.day)
# # print(today.weekday())
# # print(today.isoweekday())

# # weekday()    --> Monday 0 Sunday 6
# # isoweekday() --> Monday 1 Sunday 7

# tdelta = datetime.timedelta(days=7)
# print(today + tdelta) # shows what day will be 7 days from now
# print(today - tdelta) #vice versa

# bday = datetime.date(2024, 8, 29)
# till_bday = bday - today
# print(till_bday.total_seconds())

# t = datetime.time(9,30,45,100000)
# print(t.hour)

# t2 = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
# print(t2.date())
# print(t2.year)


# tdelta = datetime.timedelta(hours=12)
# print(t2 + tdelta)

# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)
# print(dt_utcnow)

# dt_mtn = dt_now.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

dt_mtn = datetime.datetime.now()
print(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))

# for tz in pytz.all_timezones:
#     print(tz)

