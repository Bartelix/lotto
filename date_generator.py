from datetime import date, timedelta, datetime
numbers = list(range(0, 12000))
past = 10

def lotto_date_generator(num, p=0):
    #lotto_days = [1, 3, 5]
    #lotto_days = [2, 5]
    lotto_days = [6]
    return [str(date.today() - timedelta(days = p) - timedelta(days = n)) for n in numbers if (date.today() - timedelta(days = p) - timedelta(days = n)).weekday() in lotto_days]

dates = lotto_date_generator(numbers, 13667)
print(dates)
print(len(dates), (len(dates) * 8.5) / 3600 )