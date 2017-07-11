#coding: utf-8

def days_between_dates(year1, month1, day1, year2, month2, day2):
    # 检查确保第二个日期位于第一个日期之前
    assert not date_is_before(year1, month1, day1, year2, month2, day2)
    days = 0
    while date_is_before(year1, month1, day1, year2, month2, day2):
        year, month, day = next_day(year1, month1, day1)
        days += 1

    return days
    # 检查确保传入的日期是合法的



def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def days_in_month(year, month):
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    return 30

def next_day(year, month, day):
    if day < 30:
        day += 1
    else:
        day = 1
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1

    return year, month, day

def date_is_before(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2

    return False

print next_day(2017, 12, 30)

def test():
    assert