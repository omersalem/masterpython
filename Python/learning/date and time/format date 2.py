# ----------------------------------
# -- Date and Time => Format Date --
# ----------------------------------
# https://strftime.org/ this website is used to format date and time 
# ---------------------
# %a	Sun	Weekday as locale’s abbreviated name.
# %A	Sunday	Weekday as locale’s full name.
# %w	0	Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
# %d	08	Day of the month as a zero-padded decimal number.
# %-d	8	Day of the month as a decimal number. (Platform specific)
# %b	Sep	Month as locale’s abbreviated name.
# %B	September	Month as locale’s full name.
# %m	09	Month as a zero-padded decimal number.
# %-m	9	Month as a decimal number. (Platform specific)
# %y	13	Year without century as a zero-padded decimal number.
# %Y	2013	Year with century as a decimal number.
# there are many other formats to format date and time in the website
# ----------------------------------

import datetime

myBirthday = datetime.datetime(1982, 10, 25)

print(myBirthday)
print(myBirthday.strftime("%a"))
print(myBirthday.strftime("%A"))
print(myBirthday.strftime("%b"))
print(myBirthday.strftime("%B"))

print(myBirthday.strftime("%d %B %Y"))
print(myBirthday.strftime("%d, %B, %Y"))
print(myBirthday.strftime("%d/%B/%Y"))
print(myBirthday.strftime("%d - %B - %Y"))
print(myBirthday.strftime("%B - %Y"))

print('#' * 50)

from datetime import datetime as dt

birthday = dt(1982, 10, 25)
print(birthday.strftime("%d %B %y")) #the result is 25 October 82
print(birthday.strftime("%d %B %Y")) #the result is 25 October 1982
print(birthday.strftime("%d %B %Y %H:%M:%S")) #the result is 25 October 1982 00:00:00
print(birthday.strftime("%d %B %Y %H:%M:%S %p")) #the result is 25 October 1982 00:00:00 AM

print('#' * 50)
print(dt.now().strftime("%A / %d / %B / %Y")) 